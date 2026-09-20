import Mathlib

/-!
# FDC-AUD-016 — Cadena de certificados para la suma de cortes

Archivo autocontenido: no importa archivos `.lean` sueltos ni requiere `.olean`
previos. La cadena enlaza definiciones, diez lemas y un teorema de intervalo.
Esta copia autónoma reutiliza la cadena AUD-016 (compilada en el Mac según captura).
El módulo de búsqueda AUD-017 añadido a continuación NO está compilado.

Alcance: corrección *racional* de certificados; NO formaliza la
enumeración efectiva de pares, convergencia, indecidibilidad ni T002b/T002f
en su sección racional. La extensión AUD-017 formaliza etapas finitas bajo
una enumeración asumida sobreyectiva, NO instancia todavía un enumerador concreto.
-/

namespace Continuo.Cadena

def sumaExacta (A B : Set ℚ) : Set ℚ :=
  {p | ∃ a ∈ A, ∃ b ∈ B, p = a + b}

def interior (A B : Set ℚ) (p : ℚ) : Prop :=
  ∃ a ∈ A, ∃ b ∈ B, p < a + b

def exterior (A B : Set ℚ) (p : ℚ) : Prop :=
  ∃ u : ℚ, u ∉ A ∧ ∃ v : ℚ, v ∉ B ∧ u + v < p

def inferior (A : Set ℚ) : Prop :=
  ∀ a u : ℚ, a ∈ A → u ≤ a → u ∈ A

def sinMaximo (A : Set ℚ) : Prop :=
  ∀ a : ℚ, a ∈ A → ∃ a' : ℚ, a' ∈ A ∧ a < a'

/-! ## Etapa I: del orden al control de testigos -/

/-- Un elemento interior es menor que cualquier testigo exterior. -/
theorem miembro_menor_que_exterior
    (A : Set ℚ) (hA : inferior A)
    {a u : ℚ} (ha : a ∈ A) (hu : u ∉ A) : a < u := by
  by_contra h
  exact hu (hA a u ha (le_of_not_gt h))

/-- Todo testigo estrictamente interior produce una suma puntual. -/
theorem interior_implica_suma
    (A B : Set ℚ) (p : ℚ) (hA : inferior A) :
    interior A B p → p ∈ sumaExacta A B := by
  rintro ⟨a, ha, b, hb, hp⟩
  refine ⟨p - b, hA a (p - b) ha (by linarith), b, hb, ?_⟩
  ring

/-- La ausencia de máximo convierte toda suma puntual en testigo estricto. -/
theorem suma_implica_interior
    (A B : Set ℚ) (p : ℚ) (hA : sinMaximo A) :
    p ∈ sumaExacta A B → interior A B p := by
  rintro ⟨a, ha, b, hb, hp⟩
  obtain ⟨a', ha', haa'⟩ := hA a ha
  exact ⟨a', ha', b, hb, by linarith⟩

/-- Primer resultado compuesto: equivalencia entre interior y pertenencia. -/
theorem interior_iff_suma
    (A B : Set ℚ) (p : ℚ)
    (hA : inferior A) (hNoMax : sinMaximo A) :
    interior A B p ↔ p ∈ sumaExacta A B := by
  constructor
  · exact interior_implica_suma A B p hA
  · exact suma_implica_interior A B p hNoMax

/-! ## Etapa II: el exterior separa todas las sumas -/

/-- Un certificado exterior queda estrictamente por encima de cada suma. -/
theorem exterior_acota_sumas
    (A B : Set ℚ) (p : ℚ)
    (hA : inferior A) (hB : inferior B)
    (hp : exterior A B p) :
    ∀ s ∈ sumaExacta A B, s < p := by
  rcases hp with ⟨u, hu, v, hv, huv⟩
  intro s hs
  rcases hs with ⟨a, ha, b, hb, hs⟩
  have hau : a < u := miembro_menor_que_exterior A hA ha hu
  have hbv : b < v := miembro_menor_que_exterior B hB hb hv
  rw [hs]
  linarith

/-- No puede pertenecer a la suma un racional que tiene certificado exterior. -/
theorem exterior_excluye_suma
    (A B : Set ℚ) (p : ℚ)
    (hA : inferior A) (hB : inferior B)
    (hp : exterior A B p) :
    p ∉ sumaExacta A B := by
  intro hmem
  have h : p < p := exterior_acota_sumas A B p hA hB hp p hmem
  exact (lt_irrefl p) h

/-! ## Etapa III: persistencia y separación de certificados -/

/-- Un testigo interior para q también certifica todos los p ≤ q. -/
theorem interior_hacia_abajo
    (A B : Set ℚ) (p q : ℚ)
    (hpq : p ≤ q) (hq : interior A B q) :
    interior A B p := by
  rcases hq with ⟨a, ha, b, hb, hq'⟩
  exact ⟨a, ha, b, hb, by linarith⟩

/-- Un testigo exterior para p también certifica todos los q ≥ p. -/
theorem exterior_hacia_arriba
    (A B : Set ℚ) (p q : ℚ)
    (hpq : p ≤ q) (hp : exterior A B p) :
    exterior A B q := by
  rcases hp with ⟨u, hu, v, hv, hp'⟩
  exact ⟨u, hu, v, hv, by linarith⟩

/-- No pueden coexistir certificados opuestos para el mismo racional. -/
theorem certificados_incompatibles
    (A B : Set ℚ) (p : ℚ)
    (hA : inferior A) (hB : inferior B) :
    ¬ (interior A B p ∧ exterior A B p) := by
  rintro ⟨hi, he⟩
  have hmem : p ∈ sumaExacta A B :=
    interior_implica_suma A B p hA hi
  exact (exterior_excluye_suma A B p hA hB he) hmem

/-- Cualquier certificado interior en p precede a uno exterior en q. -/
theorem certificados_ordenados
    (A B : Set ℚ) (p q : ℚ)
    (hA : inferior A) (hB : inferior B)
    (hi : interior A B p) (he : exterior A B q) :
    p < q := by
  have hmem : p ∈ sumaExacta A B :=
    interior_implica_suma A B p hA hi
  exact exterior_acota_sumas A B q hA hB he p hmem

/-! ## Etapa IV: teorema final, que reutiliza toda la cadena -/

/-- Dos certificados de extremos dan un intervalo de pertenencia y exclusión.
No se afirma que siempre existan los certificados ni que una búsqueda termine. -/
theorem intervalo_certificado
    (A B : Set ℚ) (p q : ℚ)
    (hA : inferior A) (hB : inferior B) (hNoMax : sinMaximo A)
    (hi : interior A B p) (he : exterior A B q) :
    p < q ∧
      (∀ r : ℚ, r ≤ p → r ∈ sumaExacta A B) ∧
      (∀ s : ℚ, q ≤ s → s ∉ sumaExacta A B) := by
  refine ⟨certificados_ordenados A B p q hA hB hi he, ?_, ?_⟩
  · intro r hr
    have hir : interior A B r := interior_hacia_abajo A B r p hr hi
    exact (interior_iff_suma A B r hA hNoMax).mp hir
  · intro s hs
    have hes : exterior A B s := exterior_hacia_arriba A B q s hs he
    exact exterior_excluye_suma A B s hA hB hes

end Continuo.Cadena


/-!
# AUD-018 — Búsqueda finita de certificados, instancia decidible acotada

`q : ℕ → ℚ` es una enumeración *suministrada*; `χA`, `χB` son respuestas
booleanas suministradas. Las etapas revisan una cantidad finita de pares.
`Function.Surjective q` se utiliza solo para probar que aparecerá un testigo.
No se ha construido aquí una enumeración computable concreta de ℚ.
-/

namespace Continuo.Busqueda

open Continuo.Cadena

/-- Una etapa examina pares de índices menores que `n + 1`. -/
def etapaInterior (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) : Prop :=
  ∃ i ∈ Finset.range (n + 1), ∃ j ∈ Finset.range (n + 1),
    χA (q i) = true ∧ χB (q j) = true ∧ p < q i + q j

/-- Certificado de separación estricta por arriba, en la misma etapa. -/
def etapaExterior (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) : Prop :=
  ∃ i ∈ Finset.range (n + 1), ∃ j ∈ Finset.range (n + 1),
    χA (q i) = false ∧ χB (q j) = false ∧ q i + q j < p

/-- Prueba booleana de existencia de testigo interior dentro de una etapa finita. -/
def banderaInterior (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) : Bool :=
  letI : Decidable (etapaInterior q χA χB p n) := by
    unfold etapaInterior
    infer_instance
  decide (etapaInterior q χA χB p n)

/-- Prueba booleana de existencia de testigo exterior dentro de una etapa finita. -/
def banderaExterior (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) : Bool :=
  letI : Decidable (etapaExterior q χA χB p n) := by
    unfold etapaExterior
    infer_instance
  decide (etapaExterior q χA χB p n)

/-- `some true`: interior; `some false`: exterior; `none`: continuar. -/
def salidaEtapa (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) : Option Bool :=
  if banderaInterior q χA χB p n = true then some true
  else if banderaExterior q χA χB p n = true then some false
  else none

/-- El valor booleano interior coincide con la proposición acotada. -/
theorem banderaInterior_iff (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) :
    banderaInterior q χA χB p n = true ↔ etapaInterior q χA χB p n := by
  simp [banderaInterior]

/-- El valor booleano exterior coincide con la proposición acotada. -/
theorem banderaExterior_iff (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (p : ℚ) (n : ℕ) :
    banderaExterior q χA χB p n = true ↔ etapaExterior q χA χB p n := by
  simp [banderaExterior]

/-- Una etapa interior positiva proporciona un testigo racional auténtico. -/
theorem etapaInterior_correcta
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ) (n : ℕ)
    (hA : ∀ r, χA r = true ↔ r ∈ A)
    (hB : ∀ r, χB r = true ↔ r ∈ B)
    (h : etapaInterior q χA χB p n) : interior A B p := by
  rcases h with ⟨i, _hi, j, _hj, hai, hbj, hp⟩
  exact ⟨q i, (hA _).mp hai, q j, (hB _).mp hbj, hp⟩

/-- Una etapa exterior positiva proporciona un testigo racional auténtico. -/
theorem etapaExterior_correcta
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ) (n : ℕ)
    (hA : ∀ r, χA r = false ↔ r ∉ A)
    (hB : ∀ r, χB r = false ↔ r ∉ B)
    (h : etapaExterior q χA χB p n) : exterior A B p := by
  rcases h with ⟨i, _hi, j, _hj, hai, hbj, hp⟩
  exact ⟨q i, (hA _).mp hai, q j, (hB _).mp hbj, hp⟩

/-- La extensión de una etapa no destruye un testigo interior encontrado. -/
theorem etapaInterior_monotona
    (q : ℕ → ℚ) (χA χB : ℚ → Bool) (p : ℚ)
    {n m : ℕ} (hnm : n ≤ m)
    (h : etapaInterior q χA χB p n) :
    etapaInterior q χA χB p m := by
  rcases h with ⟨i, hi, j, hj, hai, hbj, hp⟩
  refine ⟨i, ?_, j, ?_, hai, hbj, hp⟩
  · apply Finset.mem_range.mpr
    have hh := Finset.mem_range.mp hi
    omega
  · apply Finset.mem_range.mpr
    have hh := Finset.mem_range.mp hj
    omega

/-- La extensión de una etapa no destruye un testigo exterior encontrado. -/
theorem etapaExterior_monotona
    (q : ℕ → ℚ) (χA χB : ℚ → Bool) (p : ℚ)
    {n m : ℕ} (hnm : n ≤ m)
    (h : etapaExterior q χA χB p n) :
    etapaExterior q χA χB p m := by
  rcases h with ⟨i, hi, j, hj, hai, hbj, hp⟩
  refine ⟨i, ?_, j, ?_, hai, hbj, hp⟩
  · apply Finset.mem_range.mpr
    have hh := Finset.mem_range.mp hi
    omega
  · apply Finset.mem_range.mpr
    have hh := Finset.mem_range.mp hj
    omega

/-- Sobreyectividad y decididores correctos: aparece todo testigo interior. -/
theorem testigoInterior_aparece
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ)
    (hq : Function.Surjective q)
    (hA : ∀ r, χA r = true ↔ r ∈ A)
    (hB : ∀ r, χB r = true ↔ r ∈ B)
    (h : interior A B p) :
    ∃ n, etapaInterior q χA χB p n := by
  rcases h with ⟨a, ha, b, hb, hp⟩
  rcases hq a with ⟨i, hqi⟩
  rcases hq b with ⟨j, hqj⟩
  refine ⟨max i j, i, ?_, j, ?_, ?_, ?_, ?_⟩
  · exact Finset.mem_range.mpr (Nat.lt_succ_of_le (le_max_left i j))
  · exact Finset.mem_range.mpr (Nat.lt_succ_of_le (le_max_right i j))
  · rw [hqi]
    exact (hA a).mpr ha
  · rw [hqj]
    exact (hB b).mpr hb
  · simpa only [hqi, hqj] using hp

/-- Sobreyectividad y decididores correctos: aparece todo testigo exterior. -/
theorem testigoExterior_aparece
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ)
    (hq : Function.Surjective q)
    (hA : ∀ r, χA r = false ↔ r ∉ A)
    (hB : ∀ r, χB r = false ↔ r ∉ B)
    (h : exterior A B p) :
    ∃ n, etapaExterior q χA χB p n := by
  rcases h with ⟨a, ha, b, hb, hp⟩
  rcases hq a with ⟨i, hqi⟩
  rcases hq b with ⟨j, hqj⟩
  refine ⟨max i j, i, ?_, j, ?_, ?_, ?_, ?_⟩
  · exact Finset.mem_range.mpr (Nat.lt_succ_of_le (le_max_left i j))
  · exact Finset.mem_range.mpr (Nat.lt_succ_of_le (le_max_right i j))
  · rw [hqi]
    exact (hA a).mpr ha
  · rw [hqj]
    exact (hB b).mpr hb
  · simpa only [hqi, hqj] using hp

/-- Salida «interior» implica pertenencia puntual, sin usar supremos. -/
theorem salidaInterior_correcta
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ) (n : ℕ)
    (hA : ∀ r, χA r = true ↔ r ∈ A)
    (hB : ∀ r, χB r = true ↔ r ∈ B)
    (hInfA : inferior A)
    (hout : salidaEtapa q χA χB p n = some true) :
    p ∈ sumaExacta A B := by
  by_cases hi : banderaInterior q χA χB p n = true
  · apply interior_implica_suma A B p hInfA
    apply etapaInterior_correcta q χA χB A B p n hA hB
    exact (banderaInterior_iff q χA χB p n).mp hi
  · have hn : salidaEtapa q χA χB p n ≠ some true := by
      simp [salidaEtapa, hi]
    exact False.elim (hn hout)

/-- Salida «exterior» excluye pertenencia, sin usar supremos. -/
theorem salidaExterior_correcta
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ) (n : ℕ)
    (hA : ∀ r, χA r = false ↔ r ∉ A)
    (hB : ∀ r, χB r = false ↔ r ∉ B)
    (hInfA : inferior A) (hInfB : inferior B)
    (hout : salidaEtapa q χA χB p n = some false) :
    p ∉ sumaExacta A B := by
  by_cases hi : banderaInterior q χA χB p n = true
  · simp [salidaEtapa, hi] at hout
  · by_cases he : banderaExterior q χA χB p n = true
    · apply exterior_excluye_suma A B p hInfA hInfB
      apply etapaExterior_correcta q χA χB A B p n hA hB
      exact (banderaExterior_iff q χA χB p n).mp he
    · simp [salidaEtapa, hi, he] at hout

/-- Si alguno de los dos certificados existe, la salida aparece en una etapa. -/
theorem busqueda_termina_si_certificado
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ)
    (hq : Function.Surjective q)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (h : interior A B p ∨ exterior A B p) :
    ∃ n, salidaEtapa q χA χB p n ≠ none := by
  rcases h with hi | he
  · rcases testigoInterior_aparece q χA χB A B p hq hA1 hB1 hi with ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have hf : banderaInterior q χA χB p n = true :=
      (banderaInterior_iff q χA χB p n).mpr hn
    simp [salidaEtapa, hf]
  · rcases testigoExterior_aparece q χA χB A B p hq hA0 hB0 he with ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have hf : banderaExterior q χA χB p n = true :=
      (banderaExterior_iff q χA χB p n).mpr hn
    by_cases hi : banderaInterior q χA χB p n = true
    · simp [salidaEtapa, hi]
    · simp [salidaEtapa, hi, hf]

/-- En ausencia de ambos certificados, ninguna etapa produce respuesta. -/
theorem busqueda_no_termina_sin_certificados
    (q : ℕ → ℚ) (χA χB : ℚ → Bool)
    (A B : Set ℚ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (hi : ¬ interior A B p) (he : ¬ exterior A B p) :
    ∀ n, salidaEtapa q χA χB p n = none := by
  intro n
  have hni : ¬ etapaInterior q χA χB p n := by
    intro h
    exact hi (etapaInterior_correcta q χA χB A B p n hA1 hB1 h)
  have hne : ¬ etapaExterior q χA χB p n := by
    intro h
    exact he (etapaExterior_correcta q χA χB A B p n hA0 hB0 h)
  have hfi : banderaInterior q χA χB p n ≠ true := by
    intro hf
    exact hni ((banderaInterior_iff q χA χB p n).mp hf)
  have hfe : banderaExterior q χA χB p n ≠ true := by
    intro hf
    exact hne ((banderaExterior_iff q χA χB p n).mp hf)
  simp [salidaEtapa, hfi, hfe]

end Continuo.Busqueda

/-!
# FDC-AUD-019 — Enumeración ejecutable de racionales y búsqueda por combustible

Extensión autónoma: las declaraciones AUD-016–018 de arriba se mantienen
idénticas. La enumeración utiliza la instancia constructiva `Encodable ℚ`,
no una sobreyectividad postulada. `buscarHasta` recorre etapas 0,...,n.
`buscarSinCota` es una rutina parcial ejecutable: Lean la trata como opaca,
y los teoremas siguientes certifican formalmente la búsqueda por combustible,
NO la semántica del bucle opaco como ecuación del núcleo.

CANDIDATO DE FORMALIZACIÓN: sin compilación comunicada todavía.
-/

namespace Continuo.Busqueda

open Continuo.Cadena

/-- Decodifica un número natural como racional; las posiciones inválidas
    representan cero. `Encodable ℚ` contiene algoritmos de codificación. -/
def enumerarRacionales (n : ℕ) : ℚ :=
  (Encodable.decode (α := ℚ) n).getD 0

/-- Cada racional aparece en un índice: usar el código de ese racional. -/
theorem enumerarRacionales_sobreyectiva :
    Function.Surjective enumerarRacionales := by
  exact Encodable.surjective_decode_getD ℚ (0 : ℚ)

/-- El resultado de una etapa concreta no depende de enumerador abstracto. -/
def etapaConcreta (χA χB : ℚ → Bool) (p : ℚ) (n : ℕ) : Option Bool :=
  salidaEtapa enumerarRacionales χA χB p n

/-- El algoritmo total con combustible `n` revisa las etapas 0,...,n.
    No permite deducir que exista un combustible suficiente sin hipótesis. -/
def buscarHasta (χA χB : ℚ → Bool) (p : ℚ) : ℕ → Option Bool
  | 0 => etapaConcreta χA χB p 0
  | n + 1 =>
      match buscarHasta χA χB p n with
      | some b => some b
      | none => etapaConcreta χA χB p (n + 1)

/-- Cada salida acotada procede de una etapa efectivamente examinada. -/
theorem buscarHasta_tiene_testigo
    (χA χB : ℚ → Bool) (p : ℚ) :
    ∀ n b, buscarHasta χA χB p n = some b →
      ∃ k, k ≤ n ∧ etapaConcreta χA χB p k = some b := by
  intro n
  induction n with
  | zero =>
      intro b h
      exact ⟨0, le_refl 0, by simpa [buscarHasta] using h⟩
  | succ n ih =>
      intro b h
      cases hprev : buscarHasta χA χB p n with
      | none =>
          refine ⟨n + 1, le_refl _, ?_⟩
          simpa [buscarHasta, hprev] using h
      | some c =>
          have hcb : c = b := by
            simpa [buscarHasta, hprev] using h
          subst b
          obtain ⟨k, hk, hw⟩ := ih c hprev
          exact ⟨k, Nat.le_trans hk (Nat.le_succ n), hw⟩

/-- Una etapa que ya devuelve algo es detectada, a más tardar,
    al agotar exactamente ese combustible. -/
theorem buscarHasta_detecta_etapa
    (χA χB : ℚ → Bool) (p : ℚ) :
    ∀ n, etapaConcreta χA χB p n ≠ none →
      buscarHasta χA χB p n ≠ none := by
  intro n
  cases n with
  | zero =>
      intro h
      simpa [buscarHasta] using h
  | succ n =>
      intro h
      cases hprev : buscarHasta χA χB p n with
      | none =>
          simpa [buscarHasta, hprev] using h
      | some b =>
          simp [buscarHasta, hprev]

/-- La búsqueda con combustible es correcta para ambos valores devueltos.
    Solo presupone que las dos respuestas booleanas deciden cortes inferiores. -/
theorem buscarHasta_correcta
    (χA χB : ℚ → Bool) (A B : Set ℚ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (hInfA : inferior A) (hInfB : inferior B)
    (n : ℕ) (b : Bool)
    (hout : buscarHasta χA χB p n = some b) :
    (b = true → p ∈ sumaExacta A B) ∧
      (b = false → p ∉ sumaExacta A B) := by
  obtain ⟨k, _hk, hw⟩ := buscarHasta_tiene_testigo χA χB p n b hout
  constructor
  · intro hb
    subst b
    exact salidaInterior_correcta enumerarRacionales χA χB A B p k
      hA1 hB1 hInfA hw
  · intro hb
    subst b
    exact salidaExterior_correcta enumerarRacionales χA χB A B p k
      hA0 hB0 hInfA hInfB hw

/-- Ya no se presupone un enumerador exhaustivo: está construido arriba.
    Si existe un certificado, hay un combustible que produce una salida. -/
theorem existe_combustible_si_certificado
    (χA χB : ℚ → Bool) (A B : Set ℚ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (h : interior A B p ∨ exterior A B p) :
    ∃ n, buscarHasta χA χB p n ≠ none := by
  obtain ⟨n, hn⟩ :=
    busqueda_termina_si_certificado enumerarRacionales χA χB A B p
      enumerarRacionales_sobreyectiva hA1 hB1 hA0 hB0 h
  exact ⟨n, buscarHasta_detecta_etapa χA χB p n hn⟩

/-- Versión operacional parcial, de etapas sucesivas. Su definición opaca
    sirve para ejecutar, pero los resultados de corrección arriba conciernen
    a la versión total `buscarHasta`, no a esta función opaca. -/
partial def buscarSinCota (χA χB : ℚ → Bool) (p : ℚ) (n : ℕ := 0) : Bool :=
  match etapaConcreta χA χB p n with
  | some b => b
  | none => buscarSinCota χA χB p (n + 1)

end Continuo.Busqueda

/-!
FDC-AUD-020 — Puente semántico CLÁSICO con ℝ.
La sección que precede a este bloque proviene, sin modificar sus pruebas,
de FDC_T002_enumeracion_y_bucle_corregido.lean, compilada en el Mac según captura.
ESTE ARCHIVO AMPLIADO NO HA SIDO COMPILADO: los teoremas siguientes son candidatos.
La estructura ℝ es una interpretación semántica externa, NO una construcción
no circular de los reales a partir de cortes. No se verifica aquí la semántica
nuclear del partial def buscarSinCota ni los teoremas negativos T002b/T002f.
-/

namespace Continuo.Puente

open Continuo.Cadena Continuo.Busqueda

/-- Interpretación clásica de un número real como corte racional inferior estricto. -/
def corteReal (x : ℝ) : Set ℚ := {r | (r : ℝ) < x}

/-- La interpretación es cerrada hacia abajo. -/
theorem corteReal_inferior (x : ℝ) : inferior (corteReal x) := by
  intro a u ha hua
  change (a : ℝ) < x at ha
  change (u : ℝ) < x
  have hu : (u : ℝ) ≤ (a : ℝ) := by exact_mod_cast hua
  exact lt_of_le_of_lt hu ha

/-- Los testigos interiores caracterizan estar estrictamente a la izquierda. -/
theorem interior_corteReal_iff (x y : ℝ) (p : ℚ) :
    interior (corteReal x) (corteReal y) p ↔ (p : ℝ) < x + y := by
  constructor
  · rintro ⟨a, ha, b, hb, hp⟩
    change (a : ℝ) < x at ha
    change (b : ℝ) < y at hb
    have hpR : (p : ℝ) < (a : ℝ) + (b : ℝ) := by exact_mod_cast hp
    linarith
  · intro hp
    have hfirst : (p : ℝ) - y < x := by linarith
    obtain ⟨a, ha_lo, ha_hi⟩ := exists_rat_btwn hfirst
    have hsecond : (p : ℝ) - (a : ℝ) < y := by linarith
    obtain ⟨b, hb_lo, hb_hi⟩ := exists_rat_btwn hsecond
    have hpR : (p : ℝ) < (a : ℝ) + (b : ℝ) := by linarith
    have hpQ : p < a + b := by exact_mod_cast hpR
    exact ⟨a, ha_hi, b, hb_hi, hpQ⟩

/-- Los testigos exteriores caracterizan estar estrictamente a la derecha. -/
theorem exterior_corteReal_iff (x y : ℝ) (p : ℚ) :
    exterior (corteReal x) (corteReal y) p ↔ x + y < (p : ℝ) := by
  constructor
  · rintro ⟨u, hu, v, hv, hp⟩
    have hxu : x ≤ (u : ℝ) := by
      change ¬ (u : ℝ) < x at hu
      exact le_of_not_gt hu
    have hyv : y ≤ (v : ℝ) := by
      change ¬ (v : ℝ) < y at hv
      exact le_of_not_gt hv
    have hpR : (u : ℝ) + (v : ℝ) < (p : ℝ) := by exact_mod_cast hp
    linarith
  · intro hp
    have hfirst : x < (p : ℝ) - y := by linarith
    obtain ⟨u, hu_lo, hu_hi⟩ := exists_rat_btwn hfirst
    have hsecond : y < (p : ℝ) - (u : ℝ) := by linarith
    obtain ⟨v, hv_lo, hv_hi⟩ := exists_rat_btwn hsecond
    have hu : u ∉ corteReal x := by
      change ¬ (u : ℝ) < x
      linarith
    have hv : v ∉ corteReal y := by
      change ¬ (v : ℝ) < y
      linarith
    have hpR : (u : ℝ) + (v : ℝ) < (p : ℝ) := by linarith
    have hpQ : u + v < p := by exact_mod_cast hpR
    exact ⟨u, hu, v, hv, hpQ⟩

/-- Exactamente fuera de la frontera existe alguno de los certificados. -/
theorem certificados_corteReal_iff_ne (x y : ℝ) (p : ℚ) :
    (interior (corteReal x) (corteReal y) p ∨
      exterior (corteReal x) (corteReal y) p) ↔
        (p : ℝ) ≠ x + y := by
  constructor
  · intro h heq
    rcases h with hi | he
    · have hp := (interior_corteReal_iff x y p).mp hi
      exact (ne_of_lt hp) heq
    · have hp := (exterior_corteReal_iff x y p).mp he
      exact (ne_of_gt hp) heq
  · intro hne
    rcases lt_trichotomy (p : ℝ) (x + y) with hlt | heq | hgt
    · exact Or.inl ((interior_corteReal_iff x y p).mpr hlt)
    · exact False.elim (hne heq)
    · exact Or.inr ((exterior_corteReal_iff x y p).mpr hgt)

/-- El programa finito está verificado hasta algún combustible fuera de frontera. -/
theorem existe_combustible_fuera_frontera
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y)
    (hne : (p : ℝ) ≠ x + y) :
    ∃ n, buscarHasta χA χB p n ≠ none := by
  exact existe_combustible_si_certificado χA χB
    (corteReal x) (corteReal y) p hA1 hB1 hA0 hB0
    ((certificados_corteReal_iff_ne x y p).mpr hne)

/-- Si toda etapa es `none`, toda búsqueda de combustible finito también. -/
theorem buscarHasta_none_si_etapas_none
    (χA χB : ℚ → Bool) (p : ℚ)
    (h : ∀ n, etapaConcreta χA χB p n = none) :
    ∀ n, buscarHasta χA χB p n = none := by
  intro n
  induction n with
  | zero => simpa [buscarHasta] using h 0
  | succ n ih => simp [buscarHasta, ih, h (n + 1)]

/-- Exactamente en la frontera ninguna ejecución con combustible responde. -/
theorem frontera_sin_salida
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y)
    (heq : (p : ℝ) = x + y) :
    ∀ n, buscarHasta χA χB p n = none := by
  have hi : ¬ interior (corteReal x) (corteReal y) p := by
    intro h
    have hh := (interior_corteReal_iff x y p).mp h
    exact (ne_of_lt hh) heq
  have he : ¬ exterior (corteReal x) (corteReal y) p := by
    intro h
    have hh := (exterior_corteReal_iff x y p).mp h
    exact (ne_of_gt hh) heq
  apply buscarHasta_none_si_etapas_none χA χB p
  intro n
  exact busqueda_no_termina_sin_certificados
    enumerarRacionales χA χB (corteReal x) (corteReal y) p
    hA1 hB1 hA0 hB0 hi he n

/-- Caracterización exacta de la existencia de combustible, sin prometer
un decisor total de pertenencia ni probar la semántica de `partial def`. -/
theorem combustible_iff_fuera_frontera
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y) :
    (∃ n, buscarHasta χA χB p n ≠ none) ↔
      (p : ℝ) ≠ x + y := by
  constructor
  · intro h
    by_contra hne
    have heq : (p : ℝ) = x + y := by simpa using hne
    rcases h with ⟨n, hn⟩
    exact hn (frontera_sin_salida χA χB x y p
      hA1 hB1 hA0 hB0 heq n)
  · intro hne
    exact existe_combustible_fuera_frontera χA χB x y p
      hA1 hB1 hA0 hB0 hne

end Continuo.Puente

/-!
FDC-AUD-021 — Semántica RELACIONAL transparente del comparador.
Conserva exactamente el prefijo AUD-020 reportado compilado en el Mac.
`Responde` es el grafo lógico de la familia TOTAL `buscarHasta`.
NO se identifica con `partial def buscarSinCota`, que sigue siendo opaco.
Cuatro teoremas NUEVOS son candidatos: aún no se ha compilado este archivo.
-/

namespace Continuo.Semantica

open Continuo.Cadena Continuo.Busqueda Continuo.Puente

/-- Relación de respuesta: existe un combustible finito cuya salida es `some b`.
Esto define una especificación lógica de semidecisión, no una ecuación
sobre el `partial def` opaco. -/
def Responde (χA χB : ℚ → Bool) (p : ℚ) (b : Bool) : Prop :=
  ∃ n : ℕ, buscarHasta χA χB p n = some b

/-- Una respuesta del grafo tiene el sentido de pertenencia indicado. -/
theorem responde_correcta
    (χA χB : ℚ → Bool) (A B : Set ℚ) (p : ℚ) (b : Bool)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (hInfA : inferior A) (hInfB : inferior B)
    (h : Responde χA χB p b) :
    (b = true → p ∈ sumaExacta A B) ∧
      (b = false → p ∉ sumaExacta A B) := by
  rcases h with ⟨n, hn⟩
  exact buscarHasta_correcta χA χB A B p
    hA1 hB1 hA0 hB0 hInfA hInfB n b hn

/-- Dos combustibles no pueden dar respuestas booleanas contradictorias
si los decisores son correctos y los cortes están cerrados hacia abajo. -/
theorem responde_valor_unico
    (χA χB : ℚ → Bool) (A B : Set ℚ) (p : ℚ) (a b : Bool)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (hInfA : inferior A) (hInfB : inferior B)
    (ha : Responde χA χB p a)
    (hb : Responde χA χB p b) : a = b := by
  cases a <;> cases b
  · rfl
  · have hno := (responde_correcta χA χB A B p false
        hA1 hB1 hA0 hB0 hInfA hInfB ha).2 rfl
    have hsi := (responde_correcta χA χB A B p true
        hA1 hB1 hA0 hB0 hInfA hInfB hb).1 rfl
    exact False.elim (hno hsi)
  · have hsi := (responde_correcta χA χB A B p true
        hA1 hB1 hA0 hB0 hInfA hInfB ha).1 rfl
    have hno := (responde_correcta χA χB A B p false
        hA1 hB1 hA0 hB0 hInfA hInfB hb).2 rfl
    exact False.elim (hno hsi)
  · rfl

/-- El dominio exacto del grafo es la desigualdad con la frontera.
Usa ℝ clásico como modelo semántico EXTERNO, no como origen de los cortes. -/
theorem responde_iff_fuera_frontera
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y) :
    (∃ b : Bool, Responde χA χB p b) ↔ (p : ℝ) ≠ x + y := by
  constructor
  · rintro ⟨b, n, hn⟩
    apply (combustible_iff_fuera_frontera χA χB x y p
      hA1 hB1 hA0 hB0).mp
    refine ⟨n, ?_⟩
    rw [hn]
    simp
  · intro hne
    obtain ⟨n, hn⟩ := (combustible_iff_fuera_frontera χA χB x y p
      hA1 hB1 hA0 hB0).mpr hne
    cases h : buscarHasta χA χB p n with
    | none => exact False.elim (hn h)
    | some b => exact ⟨b, n, h⟩

/-- En la frontera el grafo no responde para ninguno de los dos booleanos. -/
theorem responde_ausente_en_frontera
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y)
    (heq : (p : ℝ) = x + y) :
    ∀ b : Bool, ¬ Responde χA χB p b := by
  intro b hb
  have hne := (responde_iff_fuera_frontera χA χB x y p
    hA1 hB1 hA0 hB0).mp ⟨b, hb⟩
  exact hne heq

end Continuo.Semantica


/-!
FDC-AUD-022 — sustitución operacional transparente.

La implementación canónica es ahora una FAMILIA TOTAL de observaciones finitas,
indexada por combustible. `buscarSinCota` se preserva como prototipo histórico,
pero NO se afirma una igualdad que lo relacione con la familia probada.
Cada observación termina cuando los dos decisores de entrada son computables.
La semántica parcial se define como la aparición de un resultado que, desde
entonces, permanece estable. Los siguientes teoremas son CANDIDATOS hasta
compilación local en el proyecto mathlib; NO son una certificación previa.
-/
namespace Continuo.Semantica

open Continuo.Cadena Continuo.Busqueda Continuo.Puente

/-- Implementación verificable por combustible: una observación total por `n`. -/
def programaVisible (χA χB : ℚ → Bool) (p : ℚ) : ℕ → Option Bool :=
  fun n => buscarHasta χA χB p n

/-- Una respuesta que ya apareció persiste al aumentar el combustible en uno. -/
theorem programaVisible_estable_succ
    (χA χB : ℚ → Bool) (p : ℚ) (n : ℕ) (b : Bool)
    (h : programaVisible χA χB p n = some b) :
    programaVisible χA χB p (n + 1) = some b := by
  change buscarHasta χA χB p n = some b at h
  change (match buscarHasta χA χB p n with
    | some c => some c
    | none => etapaConcreta χA χB p (n + 1)) = some b
  rw [h]

/-- Estabilidad con cualquier cantidad adicional de combustible. -/
theorem programaVisible_estable
    (χA χB : ℚ → Bool) (p : ℚ) (n k : ℕ) (b : Bool)
    (h : programaVisible χA χB p n = some b) :
    programaVisible χA χB p (n + k) = some b := by
  induction k with
  | zero => simpa using h
  | succ k ih =>
      have hs := programaVisible_estable_succ χA χB p (n + k) b ih
      simpa [Nat.add_succ] using hs

/-- La observación ejecutable implementa, por definición, el grafo AUD-021. -/
theorem programaVisible_grafo_iff
    (χA χB : ℚ → Bool) (p : ℚ) (b : Bool) :
    (∃ n, programaVisible χA χB p n = some b) ↔
      Responde χA χB p b := by
  rfl

/-- Semántica de respuesta estable: aparece una vez si y solo si
    existe una etapa desde la cual toda extensión da el mismo resultado. -/
theorem programaVisible_estabiliza_iff
    (χA χB : ℚ → Bool) (p : ℚ) (b : Bool) :
    (∃ n, programaVisible χA χB p n = some b) ↔
      (∃ n, ∀ k, programaVisible χA χB p (n + k) = some b) := by
  constructor
  · rintro ⟨n, hn⟩
    exact ⟨n, fun k => programaVisible_estable χA χB p n k b hn⟩
  · rintro ⟨n, hn⟩
    exact ⟨n, by simpa using hn 0⟩

/-- Corrección del ejecutable verificado, condicionada por decididores correctos. -/
theorem programaVisible_correcto
    (χA χB : ℚ → Bool) (A B : Set ℚ) (p : ℚ) (b : Bool)
    (hA1 : ∀ r, χA r = true ↔ r ∈ A)
    (hB1 : ∀ r, χB r = true ↔ r ∈ B)
    (hA0 : ∀ r, χA r = false ↔ r ∉ A)
    (hB0 : ∀ r, χB r = false ↔ r ∉ B)
    (hInfA : inferior A) (hInfB : inferior B)
    (h : ∃ n, programaVisible χA χB p n = some b) :
    (b = true → p ∈ sumaExacta A B) ∧
      (b = false → p ∉ sumaExacta A B) := by
  exact responde_correcta χA χB A B p b
    hA1 hB1 hA0 hB0 hInfA hInfB
    ((programaVisible_grafo_iff χA χB p b).mp h)

/-- Dominio exacto de la familia ejecutable para cortes reales clásicos. -/
theorem programaVisible_dominio_iff
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y) :
    (∃ b : Bool, ∃ n, programaVisible χA χB p n = some b) ↔
      (p : ℝ) ≠ x + y := by
  constructor
  · rintro ⟨b, hn⟩
    exact (responde_iff_fuera_frontera χA χB x y p
      hA1 hB1 hA0 hB0).mp
      ⟨b, (programaVisible_grafo_iff χA χB p b).mp hn⟩
  · intro hne
    obtain ⟨b, hb⟩ := (responde_iff_fuera_frontera χA χB x y p
      hA1 hB1 hA0 hB0).mpr hne
    exact ⟨b, (programaVisible_grafo_iff χA χB p b).mpr hb⟩

/-- En la frontera no hay resultado para ningún combustible. -/
theorem programaVisible_sin_salida_frontera
    (χA χB : ℚ → Bool) (x y : ℝ) (p : ℚ)
    (hA1 : ∀ r, χA r = true ↔ r ∈ corteReal x)
    (hB1 : ∀ r, χB r = true ↔ r ∈ corteReal y)
    (hA0 : ∀ r, χA r = false ↔ r ∉ corteReal x)
    (hB0 : ∀ r, χB r = false ↔ r ∉ corteReal y)
    (heq : (p : ℝ) = x + y) :
    ∀ b : Bool, ¬ ∃ n, programaVisible χA χB p n = some b := by
  intro b hb
  exact (responde_ausente_en_frontera χA χB x y p
    hA1 hB1 hA0 hB0 heq b)
    ((programaVisible_grafo_iff χA χB p b).mp hb)

end Continuo.Semantica
