param(
    [Parameter(Mandatory = $true)][string]$ProjectUrl,
    [Parameter(Mandatory = $true)][string]$PublishableKey
)

$ErrorActionPreference = 'Stop'
$ProjectUrl = $ProjectUrl.TrimEnd('/')
$run = 'ma-accounts-e2e-' + [guid]::NewGuid().ToString('N')

function Invoke-MARequest {
    param(
        [Parameter(Mandatory = $true)][ValidateSet('GET','POST')][string]$Method,
        [Parameter(Mandatory = $true)][string]$Path,
        [string]$Token,
        $Body,
        [hashtable]$ExtraHeaders
    )

    $headers = @{ apikey = $PublishableKey }
    if ($Token) { $headers.Authorization = "Bearer $Token" }
    if ($ExtraHeaders) {
        foreach ($key in $ExtraHeaders.Keys) { $headers[$key] = $ExtraHeaders[$key] }
    }

    $args = @{ Method = $Method; Uri = "$ProjectUrl$Path"; Headers = $headers }
    if ($null -ne $Body) {
        $args.ContentType = 'application/json'
        $args.Body = ($Body | ConvertTo-Json -Depth 20 -Compress)
    }

    Invoke-RestMethod @args
}

function ConvertTo-MAItems {
    param($Value)
    if ($null -eq $Value) { return }
    # Windows PowerShell 5.1 puede emitir un array JSON de Invoke-RestMethod
    # como un único Object[]. Write-Output fuerza la enumeración real.
    $Value | Write-Output
}

function New-AnonymousUser {
    param([string]$Label)
    $auth = Invoke-MARequest -Method POST -Path '/auth/v1/signup' -Body @{
        data = @{ ma_practica_test = $Label; run = $run }
    }
    if (-not $auth.user.id -or -not $auth.access_token) {
        throw "Anonymous sign-in failed for $Label"
    }
    $auth
}

$u1 = New-AnonymousUser 'u1'
$u2 = New-AnonymousUser 'u2'

$u1Identity = Invoke-MARequest -Method GET -Path '/auth/v1/user' -Token $u1.access_token
$u2Identity = Invoke-MARequest -Method GET -Path '/auth/v1/user' -Token $u2.access_token

if ($u1Identity.id -ne $u1.user.id -or $u2Identity.id -ne $u2.user.id) {
    throw 'Auth token identity does not match the user returned at anonymous sign-in.'
}
if ($u1Identity.id -eq $u2Identity.id) {
    throw 'Anonymous sign-in returned the same user twice.'
}

$first = @(ConvertTo-MAItems (Invoke-MARequest -Method POST -Path '/rest/v1/rpc/ma_record_rated_exercise' -Token $u1.access_token -Body @{
    p_exercise_id = 'MAP-DEMO-005'
    p_area = 'algebra'
    p_exercise_rating = 1200
    p_outcome = 1
    p_rating_policy = 'first-attempt-v03'
}))[0]

$duplicate = @(ConvertTo-MAItems (Invoke-MARequest -Method POST -Path '/rest/v1/rpc/ma_record_rated_exercise' -Token $u1.access_token -Body @{
    p_exercise_id = 'MAP-DEMO-005'
    p_area = 'algebra'
    p_exercise_rating = 1200
    p_outcome = 1
    p_rating_policy = 'first-attempt-v03'
}))[0]

if ($first.applied -ne $true -or $first.rating_after -ne 1212) {
    throw 'First Elo event did not produce the expected server result.'
}
if ($duplicate.applied -ne $false -or $duplicate.rating_after -ne 1212) {
    throw 'Duplicate Elo event was not blocked.'
}

$finished = (Get-Date).ToUniversalTime().ToString('o')
Invoke-MARequest -Method POST -Path '/rest/v1/practice_sessions' -Token $u1.access_token -ExtraHeaders @{ Prefer = 'return=minimal' } -Body @{
    user_id = $u1.user.id
    exercise_id = 'MAP-DEMO-005'
    area = 'algebra'
    mode = 'challenge'
    payload = @{
        id = 'MAP-DEMO-005'
        title = 'Live Auth test U1'
        area = 'algebra'
        mode = 'challenge'
        correct = 2
        total = 2
        trace = @()
        finishedAt = $finished
    }
    finished_at = $finished
} | Out-Null

$u2BeforeRatings = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/user_ratings?select=area,rating' -Token $u2.access_token))
$u2BeforeRated = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/rated_exercises?select=exercise_id' -Token $u2.access_token))
$u2BeforeSessions = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/practice_sessions?select=id' -Token $u2.access_token))

if ($u2BeforeRatings.Count -ne 0 -or $u2BeforeRated.Count -ne 0 -or $u2BeforeSessions.Count -ne 0) {
    throw "RLS leak: U2 sees ratings=$($u2BeforeRatings.Count), rated=$($u2BeforeRated.Count), sessions=$($u2BeforeSessions.Count)."
}

$import = @(ConvertTo-MAItems (Invoke-MARequest -Method POST -Path '/rest/v1/rpc/ma_import_local_progress' -Token $u2.access_token -Body @{
    p_snapshot = @{
        version = 1
        createdAt = (Get-Date).ToUniversalTime().ToString('o')
        ratings = @{ algebra = 1333 }
        ratedIds = @('MAP-DEMO-006')
        history = @()
    }
}))[0]

$u2Elo = @(ConvertTo-MAItems (Invoke-MARequest -Method POST -Path '/rest/v1/rpc/ma_record_rated_exercise' -Token $u2.access_token -Body @{
    p_exercise_id = 'MAP-DEMO-005'
    p_area = 'algebra'
    p_exercise_rating = 1200
    p_outcome = 0
    p_rating_policy = 'first-attempt-v03'
}))[0]

$crossWriteRejected = $false
try {
    Invoke-MARequest -Method POST -Path '/rest/v1/practice_sessions' -Token $u2.access_token -ExtraHeaders @{ Prefer = 'return=minimal' } -Body @{
        user_id = $u1.user.id
        exercise_id = 'MAP-DEMO-099'
        area = 'algebra'
        mode = 'training'
        payload = @{ id = 'MAP-DEMO-099'; area = 'algebra'; mode = 'training' }
    } | Out-Null
} catch {
    $crossWriteRejected = $true
}
if (-not $crossWriteRejected) { throw 'RLS allowed a cross-user write.' }

$u1Ratings = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/user_ratings?select=area,rating' -Token $u1.access_token))
$u1Rated = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/rated_exercises?select=exercise_id' -Token $u1.access_token))
$u2Ratings = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/user_ratings?select=area,rating' -Token $u2.access_token))
$u2Rated = @(ConvertTo-MAItems (Invoke-MARequest -Method GET -Path '/rest/v1/rated_exercises?select=exercise_id&order=exercise_id' -Token $u2.access_token))

if ($u1Ratings.Count -ne 1 -or $u1Ratings[0].rating -ne 1212 -or $u1Rated.Count -ne 1) {
    throw 'U1 final state is inconsistent.'
}
if ($u2Ratings.Count -ne 1 -or $u2Ratings[0].rating -ne 1317 -or $u2Rated.Count -ne 2) {
    throw 'U2 final state is inconsistent.'
}

[PSCustomObject]@{
    Status = 'PASS'
    Run = $run
    U1UserId = $u1.user.id
    U2UserId = $u2.user.id
    U1FirstApplied = $first.applied
    U1DuplicateApplied = $duplicate.applied
    U1Rating = $u1Ratings[0].rating
    U2ImportedRatings = $import.imported_ratings
    U2ImportedRatedIds = $import.imported_rated_ids
    U2Rating = $u2Ratings[0].rating
    CrossUserWriteRejected = $crossWriteRejected
}

Write-Host ''
Write-Host 'IMPORTANTE: este test crea dos usuarios anónimos reales.' -ForegroundColor Yellow
Write-Host 'Pega la salida anterior en el chat para eliminarlos del proyecto de desarrollo.' -ForegroundColor Yellow
