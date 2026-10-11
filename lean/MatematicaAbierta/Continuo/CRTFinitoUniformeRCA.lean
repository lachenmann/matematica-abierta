import MatematicaAbierta.Continuo.PasoEstadoCRTRCA

/-! M11/C10: fixed-b finite CRT in the declared calculus, conditional on
the explicit bounded finite data D and CM. No new inference constructors.
The bridge reuses M05 Derives.exNI through the existing ordered embed,
then M09 exNE and I-Sigma1. Recoding b, Trace and global adequacy are not
claimed. Product-history beta coding is not a premise of this proof. -/
namespace MatematicaAbierta.Continuo.CRTFinitoUniformeRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA TrazasInduccionRCA
open ProductoAcumuladoRCA InvarianteCRTParcialRCA InversosFuturosRCA
open ActualizacionCodigoCRTRCA PasoEstadoCRTRCA
abbrev LogicalProof := CalculoExistencialRCA.Proof

def guardedResult : Formula := .exB 75 cap
  (.imp (.le (.succ k) (.succ N)) (state (.succ k) nextP (.var 75) cap))
def guardΓ : List Formula := [matrix,MultiploComunUniformeRCA.cm N b,residueData]

def atStateStep {Γ : List Formula}
    (hd : Proof Γ residueData) (hc : Proof Γ (MultiploComunUniformeRCA.cm N b))
    (hs : Proof Γ (state k p A C)) (hk : Proof Γ (.le k N)) : Proof Γ result := by
  have h0 := Proof.allE 0 N (by decide) stateStep
  have h1 := Proof.allE 3 k (by decide) h0
  have h2 := Proof.allE 4 R (by decide) h1
  have h3 := Proof.allE 9 b (by decide) h2
  have h4 := Proof.allE 50 p (by decide) h3
  have h5 := Proof.allE 51 A (by decide) h4
  have h6 := Proof.allE 52 C (by decide) h5
  exact .impE (.impE (.impE (.impE (SelectoresInternosRCA.closed h6) hd) hc) hs) hk

def addGuard {Γ : List Formula} (fresh : freshNum 75 Γ = true)
    (hs : Proof Γ result) : Proof Γ guardedResult := by
  apply Proof.exBE 75 cap fresh (by decide) (by decide) hs
  apply Proof.exBI 75 cap (.var 75) (by decide) (push hyp)
  apply Proof.impI
  exact push hyp

def guardedStep : Proof guardΓ guardedResult := by
  apply Proof.orderCases k N
  · have hk : Proof (.lt k N :: guardΓ) (.le k N) := .ltLe hyp
    have mat : Proof (.lt k N :: guardΓ) matrix := push hyp
    have hs : Proof (.lt k N :: guardΓ) (state k p A C) :=
      .impE mat (.leTrans hk (leSucc N))
    exact addGuard (by decide) (atStateStep rca_ctx rca_ctx hs hk)
  · have hk : Proof (.eq k N :: guardΓ) (.le k N) :=
      .leRewrite (.eqSymm hyp) (eqRefl _) (leRefl N)
    have mat : Proof (.eq k N :: guardΓ) matrix := push hyp
    have hs : Proof (.eq k N :: guardΓ) (state k p A C) :=
      .impE mat (.leTrans hk (leSucc N))
    exact addGuard (by decide) (atStateStep rca_ctx rca_ctx hs hk)
  · apply Proof.exBI 75 cap (.lit 0) (by decide)
      (.leLtTrans (.zeroLe (.lit 1)) capAboveOne)
    apply Proof.impI
    exact .botE (.ltIrrefl (.ltLeTrans (ltSucc k) (.leTrans hyp (.ltSuccLe (push hyp)))))

/-- Bounded elimination followed by ordinary unbounded introductions. The
premise of exNI is a genuine context hypothesis of a derivation branch,
not an ambient mathematical assertion or a new coding axiom. -/
def numericGuarded : Proof guardΓ (invariant.subst 3 (.succ k)) := by
  apply Proof.exBE 75 cap (by decide) (by decide) (by decide) guardedStep
  apply Proof.embed
  apply Derives.exNI 50 nextP (by decide)
  apply Derives.exNI 51 (.var 75) (by decide)
  apply Derives.exNI 52 cap (by decide)
  exact .hypothesis List.mem_cons_self

def logicalΓ : List Formula := [residueData,MultiploComunUniformeRCA.cm N b]
def eliminationΓ : List Formula := [matrix,.exN 52 matrix,.exN 51 (.exN 52 matrix),invariant] ++ logicalΓ
def oldToElimination : Proof eliminationΓ (invariant.subst 3 (.succ k)) :=
  .weaken (by
    intro f hf
    change f ∈ [matrix,MultiploComunUniformeRCA.cm N b,residueData] at hf
    cases hf with
    | head => exact List.mem_cons_self
    | tail _ h =>
      cases h with
      | head => repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem
      | tail _ h =>
        cases h with
        | head => repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem
        | tail _ h => cases h) numericGuarded

/-- EXACT M10 fullStepGoal, under only CM and the declared finite data. -/
def fullStep : LogicalProof logicalΓ fullStepGoal := by
  apply CalculoExistencialRCA.Proof.allI 3 (by decide)
  apply CalculoExistencialRCA.Proof.impI
  apply CalculoExistencialRCA.Proof.exNE 50 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNE 51 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNE 52 (by decide) (by decide) CalculoExistencialRCA.hyp
  exact .embed oldToElimination

def uniformInvariant : LogicalProof logicalΓ (.allN 3 invariant) :=
  .sigma1Induction 3 invariantSigma1 (by decide) (by decide) (by decide)
    (CalculoExistencialRCA.closed base) fullStep

def finalMatrix : Formula := matrix.subst 3 (.succ N)
def extractionΓ : List Formula := [finalMatrix,.exN 52 finalMatrix,
  .exN 51 (.exN 52 finalMatrix)] ++ logicalΓ
def finalReadings : Proof extractionΓ (readings (.succ N) A b R) := by
  have hs : Proof extractionΓ (state (.succ N) p A C) :=
    .impE (hyp : Proof extractionΓ _) (leRefl (.succ N))
  exact .andL (.andR (.andR (.andR (.andR hs))))
def finiteCRT : LogicalProof logicalΓ (.exN 51 (readings (.succ N) A b R)) := by
  have atEnd : LogicalProof logicalΓ (invariant.subst 3 (.succ N)) :=
    .allE 3 (.succ N) (by decide) uniformInvariant
  apply CalculoExistencialRCA.Proof.exNE 50 (by decide) (by decide) atEnd
  apply CalculoExistencialRCA.Proof.exNE 51 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNE 52 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNI 51 A (by decide)
  exact .embed finalReadings

/-- EXACT M10 fixedBCRTGoal: forall N,R,b, CM(N,b) -> residueData(D) ->
exists A, all D-prescribed readings at 0,...,N. Set parameter D is free. -/
def fixedBCRT : LogicalProof [] fixedBCRTGoal :=
  .allI 0 rfl (.allI 4 rfl (.allI 9 rfl (.impI (.impI finiteCRT))))

example : guardedResult.bounded = true := by decide
example : freshNum 75 guardΓ = true := by decide
example : (invariant.subst 3 (.succ k)).numFree.contains 75 = false := by decide
example : freshNum 50 [invariant,residueData,MultiploComunUniformeRCA.cm N b] = true := by decide
example : freshNum 51 [.exN 51 (.exN 52 matrix),invariant,residueData,MultiploComunUniformeRCA.cm N b] = true := by decide
example : freshNum 52 [.exN 52 matrix,.exN 51 (.exN 52 matrix),invariant,residueData,MultiploComunUniformeRCA.cm N b] = true := by decide
example : invariant.safe 3 (.succ N) = true := by decide
example : freshNum 3 logicalΓ = true := by decide
example : fixedBCRTGoal.numFree = [] := by decide
example : fixedBCRTGoal.setFree.all (· == 2) = true := by decide
example : fixedBCRTGoal.setFree.contains 2 = true := by decide
#print axioms guardedStep
#print axioms numericGuarded
#print axioms fullStep
#print axioms uniformInvariant
#print axioms fixedBCRT
#eval ("guarded_bounded_state_step", profile guardedStep)
#eval ("ordinary_existential_numeric_bridge", profile numericGuarded)
#eval ("full_sigma1_crt_invariant_step", CalculoExistencialRCA.profile fullStep)
#eval ("uniform_sigma1_crt_invariant", CalculoExistencialRCA.profile uniformInvariant)
#eval ("fixed_b_uniform_finite_crt", CalculoExistencialRCA.profile fixedBCRT)
end MatematicaAbierta.Continuo.CRTFinitoUniformeRCA
