import MatematicaAbierta.Continuo.CRTCanalesSeparadosRCA
import MatematicaAbierta.Continuo.TotalidadTrazaRCA

/-! M12: finite, bounded selectors for recoding two numerical beta traces.
Only Delta1 comprehension supplies sets. Their totality and functionality
must be proved from Trace and the explicit admissible-bit antecedent. -/
namespace MatematicaAbierta.Continuo.DatosRecodificacionBetaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA
open EmparejamientoInternoRCA ContratoExtensionBetaRCA
open CRTCanalesSeparadosRCA

def successorValue : Channel → Term
  | .u => nextU (.var 1) (.var 7)
  | .d => nextD (.var 2)
def oldReading (c : Channel) (i v : Term) : Formula :=
  .conj (.lt v valueBound) (beta (codeA c) (codeB c) i v)
def relation (c : Channel) (i v : Term) : Formula :=
  .conj (.le i newK) (.conj (.lt v newT)
    (.conj (.imp (.le i stageBound) (oldReading c i v))
      (.imp (.eq i newK) (.eq v (successorValue c)))))
def body (c : Channel) : Formula :=
  .conj (.eq (.var 100) (pair (.var 101) (.var 102)))
    (relation c (.var 101) (.var 102))
def matrix (c : Channel) : Formula :=
  .exB 101 (.succ (.var 100)) (.exB 102 (.succ (.var 100)) (body c))
def spec (c : Channel) : Formula :=
  .allN 100 (iffF (.member (.var 100) (dataSet c)) (matrix c))

def finiteDataExists (c : Channel) : Proof [] (.exS (dataSet c) (spec c)) :=
  .embed (.delta1Comprehension 100 (dataSet c)
    (.bounded (by cases c <;> decide)) (.bounded (by cases c <;> decide))
    rfl (by cases c <;> decide) (by cases c <;> decide)
    (.allI 100 rfl (.andI (.impI (.hypothesis List.mem_cons_self))
      (.impI (.hypothesis List.mem_cons_self)))))

def member (c : Channel) (i v : Term) : Formula := .member (pair i v) (dataSet c)
def encode {Γ : List Formula} (c : Channel)
    (hs : Proof Γ (spec c)) (hr : Proof Γ (relation c (.var 16) (.var 17))) :
    Proof Γ (member c (.var 16) (.var 17)) := by
  have he := Proof.allE 100 (pair (.var 16) (.var 17)) (by cases c <;> decide) hs
  apply Proof.impE (.andR he)
  apply Proof.exBI 101 (.succ (pair (.var 16) (.var 17))) (.var 16)
    (by cases c <;> decide) (firstProjectionBound _ _)
  apply Proof.exBI 102 (.succ (pair (.var 16) (.var 17))) (.var 17)
    (by cases c <;> decide) (secondProjectionBound _ _)
  cases c <;> exact .andI (eqRefl _) hr

def targetValue (second : Bool) : Term := if second then .var 19 else .var 17
def decodeΓ (c : Channel) (second : Bool) : List Formula :=
  [member c (.var 16) (targetValue second),spec c]
def pointBody (c : Channel) (second : Bool) : Formula :=
  (body c).subst 100 (pair (.var 16) (targetValue second))
def witnessΓ (c : Channel) (second : Bool) : List Formula :=
  [pointBody c second,.lt (.var 102) (.succ (pair (.var 16) (targetValue second))),
    .exB 102 (.succ (pair (.var 16) (targetValue second))) (pointBody c second),
    .lt (.var 101) (.succ (pair (.var 16) (targetValue second)))] ++ decodeΓ c second

def decodeWitness (c : Channel) (second : Bool) :
    Proof (witnessΓ c second) (relation c (.var 16) (targetValue second)) := by
  have hw : Proof (witnessΓ c second) (pointBody c second) := hyp
  have he : Proof (witnessΓ c second)
      (.eq (pair (.var 16) (targetValue second)) (pair (.var 101) (.var 102))) := by
    cases c <;> cases second <;> exact .andL hw
  have hi := pairInjectiveOpen (.var 16) (targetValue second) (.var 101) (.var 102) he
  have hr : Proof (witnessΓ c second) (relation c (.var 101) (.var 102)) := by
    cases c <;> cases second <;> exact .andR hw
  have hr1 : Proof (witnessΓ c second) (relation c (.var 16) (.var 102)) := by
    let rp := relation c (.var 103) (.var 102)
    cases c <;> cases second <;>
      exact Proof.eqSubst rp 103
        (.var 101) (.var 16) (by decide) (by decide) (.eqSymm (.andL hi)) hr
  let rq := relation c (.var 16) (.var 104)
  let w := targetValue second
  cases c <;> cases second <;>
    exact Proof.eqSubst rq 104
      (.var 102) w (by decide) (by decide) (.eqSymm (.andR hi)) hr1

def decode (c : Channel) (second : Bool) : Proof (decodeΓ c second)
    (relation c (.var 16) (targetValue second)) := by
  have hs := Proof.allE 100 (pair (.var 16) (targetValue second))
    (by cases c <;> cases second <;> decide) (push hyp : Proof (decodeΓ c second) (spec c))
  have hm := Proof.impE (.andL hs) hyp
  apply Proof.exBE 101 (.succ (pair (.var 16) (targetValue second)))
    (by cases c <;> cases second <;> decide)
    (by cases c <;> cases second <;> decide)
    (by cases second <;> decide) hm
  apply Proof.exBE 102 (.succ (pair (.var 16) (targetValue second)))
    (by cases c <;> cases second <;> decide)
    (by cases c <;> cases second <;> decide)
    (by cases second <;> decide) hyp
  exact decodeWitness c second

def oldUnique (c : Channel) : Proof []
    (.imp (beta (codeA c) (codeB c) (.var 16) (.var 17))
      (.imp (beta (codeA c) (codeB c) (.var 16) (.var 19))
        (.eq (.var 17) (.var 19)))) := by
  let a := codeA c
  let b := codeB c
  cases c <;> exact Proof.allE 19 (.var 19) (by decide)
    (Proof.allE 18 (.var 17) (by decide)
      (Proof.allE 0 (.var 16) (by decide)
        (Proof.allE 9 b (by decide)
          (Proof.allE 8 a (by decide) betaUniqueFresh))))

def relationUnique {Γ : List Formula} (c : Channel)
    (h1 : Proof Γ (relation c (.var 16) (.var 17)))
    (h2 : Proof Γ (relation c (.var 16) (.var 19))) : Proof Γ (.eq (.var 17) (.var 19)) := by
  apply Proof.orderCases (.var 16) stageBound
  · have hk : Proof (.lt (.var 16) stageBound :: Γ) (.le (.var 16) stageBound) := .ltLe hyp
    have o1 := Proof.impE (.andL (.andR (.andR (push h1)))) hk
    have o2 := Proof.impE (.andL (.andR (.andR (push h2)))) hk
    exact .impE (.impE (closed (oldUnique c)) (.andR o1)) (.andR o2)
  · have hk : Proof (.eq (.var 16) stageBound :: Γ) (.le (.var 16) stageBound) :=
      .leRewrite (.eqSymm hyp) (eqRefl _) (leRefl _)
    have o1 := Proof.impE (.andL (.andR (.andR (push h1)))) hk
    have o2 := Proof.impE (.andL (.andR (.andR (push h2)))) hk
    exact .impE (.impE (closed (oldUnique c)) (.andR o1)) (.andR o2)
  · have he : Proof (.lt stageBound (.var 16) :: Γ) (.eq (.var 16) newK) :=
      .leAntisymm (.andL (push h1)) (.ltSuccLe hyp)
    have e1 := Proof.impE (.andR (.andR (.andR (push h1)))) he
    have e2 := Proof.impE (.andR (.andR (.andR (push h2)))) he
    exact .eqTrans e1 (.eqSymm e2)

def oldRelation {Γ : List Formula} (c : Channel) (v : Term)
    (hk : Proof Γ (.le (.var 16) stageBound))
    (hv : Proof Γ (.lt v valueBound))
    (hb : Proof Γ (beta (codeA c) (codeB c) (.var 16) v)) :
    Proof Γ (relation c (.var 16) v) := by
  apply Proof.andI (.leTrans hk (leSucc _))
  apply Proof.andI (.ltTrans hv (oldBoundBelow _))
  apply Proof.andI
  · apply Proof.impI
    exact .andI (push hv) (push hb)
  · apply Proof.impI
    have hn : Proof (.eq (.var 16) newK :: Γ) (.lt stageBound (.var 16)) :=
      .ltRewrite (eqRefl _) (.eqSymm hyp) (ltSucc _)
    exact .botE (.ltIrrefl (.ltLeTrans hn (push hk)))

def successorBound {Γ : List Formula} (c : Channel)
    (he : Proof Γ extensionInput) : Proof Γ (.lt (successorValue c) newT) := by
  have hu := Proof.andL (Proof.andR he)
  have hd := Proof.andL (Proof.andR (Proof.andR he))
  have hb := Proof.andR (Proof.andR (Proof.andR (Proof.andR (Proof.andR (Proof.andR he)))))
  cases c
  · exact nextUBound _ _ _ hu hb
  · exact nextDBound _ _ hd

def lastRelation {Γ : List Formula} (c : Channel)
    (he : Proof Γ extensionInput) : Proof Γ (relation c newK (successorValue c)) := by
  apply Proof.andI (leRefl _)
  apply Proof.andI (successorBound c he)
  apply Proof.andI
  · apply Proof.impI
    exact .botE (.ltIrrefl (.ltLeTrans (ltSucc stageBound) hyp))
  · apply Proof.impI
    exact eqRefl _

def totalFormula (c : Channel) : Formula :=
  .exB 17 newT (relation c (.var 16) (.var 17))
def oldTotalΓ : List Formula := [.le (.var 16) stageBound,.le (.var 16) newK,extensionInput]
def oldPair : Formula :=
  .conj (beta (.var 8) (.var 9) (.var 16) (.var 121))
    (beta (.var 10) (.var 11) (.var 16) (.var 122))
def oldLeafΓ : List Formula := [oldPair,.lt (.var 122) valueBound,
  .exB 2 valueBound (.conj (beta (.var 8) (.var 9) (.var 16) (.var 121))
    (beta (.var 10) (.var 11) (.var 16) (.var 2))),.lt (.var 121) valueBound] ++ oldTotalΓ

def oldTotalLeaf (c : Channel) : Proof oldLeafΓ (totalFormula c) := by
  let w : Term := match c with | .u => .var 121 | .d => .var 122
  have hw : Proof oldLeafΓ (.lt w valueBound) := by
    cases c
    · exact rca_ctx
    · exact rca_ctx
  have hb : Proof oldLeafΓ (beta (codeA c) (codeB c) (.var 16) w) := by
    cases c
    · exact .andL (hyp : Proof oldLeafΓ oldPair)
    · exact .andR (hyp : Proof oldLeafΓ oldPair)
  have hk : Proof oldLeafΓ (.le (.var 16) stageBound) := rca_ctx
  have hr := oldRelation c w hk hw hb
  cases c <;> exact Proof.exBI 17 newT w (by decide)
    (.ltTrans hw (oldBoundBelow _)) hr

def oldTotal (c : Channel) : Proof oldTotalΓ (totalFormula c) := by
  have ht : Proof oldTotalΓ finiteTraceMatrix :=
    .andL (rca_ctx : Proof oldTotalΓ extensionInput)
  have htotal := Proof.impE (closed TotalidadTrazaRCA.traceTotal) ht
  have hi := Proof.allE 0 (.var 16) (by decide) htotal
  have hp := Proof.impE hi (hyp : Proof oldTotalΓ (.le (.var 16) stageBound))
  apply Proof.exBErename 1 121 valueBound (by decide) (by cases c <;> decide)
    (by decide) (by decide) hp
  apply Proof.exBErename 2 122 valueBound (by decide) (by cases c <;> decide)
    (by decide) (by decide) hyp
  exact oldTotalLeaf c

def totalΓ : List Formula := [.le (.var 16) newK,extensionInput]
def totalRelations (c : Channel) : Proof totalΓ (totalFormula c) := by
  apply Proof.orderCases (.var 16) stageBound
  · have cut : Proof totalΓ (.imp (.le (.var 16) stageBound) (totalFormula c)) := .impI (oldTotal c)
    exact .impE (push cut) (.ltLe hyp)
  · have cut : Proof totalΓ (.imp (.le (.var 16) stageBound) (totalFormula c)) := .impI (oldTotal c)
    exact .impE (push cut) (.leRewrite (.eqSymm hyp) (eqRefl _) (leRefl _))
  · have he : Proof (.lt stageBound (.var 16) :: totalΓ) (.eq newK (.var 16)) :=
      .leAntisymm (.ltSuccLe hyp) (push hyp)
    have hi : Proof (.lt stageBound (.var 16) :: totalΓ) extensionInput := rca_ctx
    have hr := lastRelation c hi
    let rp := relation c (.var 103) (successorValue c)
    have here : Proof (.lt stageBound (.var 16) :: totalΓ)
        (relation c (.var 16) (successorValue c)) := by
      cases c <;> exact Proof.eqSubst rp 103 newK (.var 16) (by decide) (by decide) he hr
    let w := successorValue c
    cases c <;> exact Proof.exBI 17 newT w (by decide) (successorBound _ hi) here

def residueBelowModule {Γ : List Formula}
    (hb : Proof Γ (.lt newT newB)) (hv : Proof Γ (.lt (.var 17) newT)) :
    Proof Γ (.lt (.var 17) (LecturasBetaRCA.modulus (.var 16) newB)) := by
  have ho : Proof Γ (.le (.lit 1) (.succ (.var 16))) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _)
      (.ltSuccLe (.leLtTrans (.zeroLe _) (ltSucc _)))
  have e : EqProof (.succ (.var 16)) (.add (.var 16) (.lit 1)) :=
    .symm (.trans (.add (.refl _) (.literalSucc 0))
      (.trans (.addSucc _ _) (.succ (.addZero _))))
  have ho' := Proof.leRewrite (eqRefl _) (ax e) ho
  have hm : Proof Γ (.le newB (.mul (.add (.var 16) (.lit 1)) newB)) :=
    .leRewrite (ax (mulOneLeft _)) (eqRefl _) (.leMulRight newB ho')
  exact .ltLeTrans (.ltTrans hv hb) (.leTrans hm (leLeftAdd _ (.lit 1)))

def belowSuccessor {Γ : List Formula} (i k : Term)
    (h : Proof Γ (.lt i (.succ k))) : Proof Γ (.le i k) := by
  apply Proof.orderCases i k
  · exact .ltLe hyp
  · exact .leRewrite (.eqSymm hyp) (eqRefl _) (leRefl _)
  · exact .botE (.ltIrrefl (.ltLeTrans (push h) (.ltSuccLe hyp)))

def dataΓ (c : Channel) : List Formula := [spec c,.lt newT newB,extensionInput]
def dataBody (c : Channel) : Formula :=
  .conj (member c (.var 16) (.var 17))
    (.conj (.lt (.var 17) (LecturasBetaRCA.modulus (.var 16) newB))
      (.allB 19 newT (.imp (member c (.var 16) (.var 19)) (.eq (.var 17) (.var 19)))))
def dataLeafΓ (c : Channel) : List Formula :=
  [relation c (.var 16) (.var 17),.lt (.var 17) newT,
    .lt (.var 16) (.succ newK)] ++ dataΓ c

def dataLeaf (c : Channel) : Proof (dataLeafΓ c) (dataBody c) := by
  have hr : Proof (dataLeafΓ c) (relation c (.var 16) (.var 17)) := hyp
  have hs : Proof (dataLeafΓ c) (spec c) := rca_ctx
  have hb : Proof (dataLeafΓ c) (.lt newT newB) := rca_ctx
  apply Proof.andI (encode c hs hr)
  apply Proof.andI (residueBelowModule hb (.andL (.andR hr)))
  apply Proof.allBI 19 newT (by cases c <;> decide) (by decide)
  apply Proof.impI
  have ds : Proof (member c (.var 16) (.var 19) :: .lt (.var 19) newT :: dataLeafΓ c)
      (.imp (spec c) (.imp (member c (.var 16) (.var 19)) (relation c (.var 16) (.var 19)))) :=
    closed (Proof.impI (Proof.impI (decode c true)))
  have hsp : Proof (member c (.var 16) (.var 19) :: .lt (.var 19) newT :: dataLeafΓ c) (spec c) := rca_ctx
  have hr2 := Proof.impE (Proof.impE ds hsp) hyp
  exact relationUnique c (push (push hr)) hr2

def residueDataFromTrace (c : Channel) : Proof (dataΓ c) (data c) := by
  have ht : Proof [] (.imp extensionInput (.imp (.le (.var 16) newK) (totalFormula c))) :=
    .impI (.impI (totalRelations c))
  apply Proof.allBI 16 (.succ newK) (by cases c <;> decide) (by decide)
  change Proof (.lt (.var 16) (.succ newK) :: dataΓ c) (.exB 17 newT (dataBody c))
  have he : Proof (.lt (.var 16) (.succ newK) :: dataΓ c) extensionInput := rca_ctx
  have hk := belowSuccessor (.var 16) newK (hyp : Proof (.lt (.var 16) (.succ newK) :: dataΓ c) _)
  have hall := Proof.impE (Proof.impE (closed ht) he) hk
  apply Proof.exBE 17 newT (by cases c <;> decide) (by cases c <;> decide) (by decide) hall
  apply Proof.exBI 17 newT (.var 17) (by cases c <;> decide) (push hyp)
  cases c
  · exact dataLeaf .u
  · exact dataLeaf .d

-- Explicit upper bound on every represented residue. Totality and uniqueness
-- are separate claims: bounded comprehension alone does not grant either.
def valueBoundProof {Γ : List Formula} (c : Channel)
    (hr : Proof Γ (relation c (.var 16) (.var 17))) :
    Proof Γ (.lt (.var 17) newT) := .andL (.andR hr)

example : (matrix .u).bounded = true := by decide
example : (matrix .d).bounded = true := by decide
example : (matrix .u).setFree = [] := by decide
example : (matrix .d).setFree = [] := by decide
example : freshSet 3 [extensionInput] = true := by decide
example : freshSet 4 [extensionInput] = true := by decide
example : extensionInput.setFree.all (· == 2) = true := by decide
example : (matrix .u).safe 100 (pair (.var 101) (.var 102)) = false := by decide
-- Safe substitution at the specification is possible because the selectors
-- 101/102 are different from the reading variables 16/17.
#print axioms finiteDataExists
#print axioms encode
#print axioms decode
#print axioms oldUnique
#print axioms relationUnique
#print axioms valueBoundProof
#print axioms oldRelation
#print axioms successorBound
#print axioms lastRelation
#print axioms residueBelowModule
#print axioms residueDataFromTrace
#print axioms oldTotal
#print axioms totalRelations
#eval ("DU_full_residue_contract", profile (Proof.impI (Proof.impI (Proof.impI (residueDataFromTrace .u)))))
#eval ("DD_full_residue_contract", profile (Proof.impI (Proof.impI (Proof.impI (residueDataFromTrace .d)))))
#eval ("DU_internal_totality_from_trace", profile (Proof.impI (Proof.impI (totalRelations .u))))
#eval ("DD_internal_totality_from_trace", profile (Proof.impI (Proof.impI (totalRelations .d))))
#eval ("finite_DU_comprehension", profile (finiteDataExists .u))
#eval ("finite_DD_comprehension", profile (finiteDataExists .d))
end MatematicaAbierta.Continuo.DatosRecodificacionBetaRCA
