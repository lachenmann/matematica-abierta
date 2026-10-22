import MatematicaAbierta.Continuo.ActualizacionCodigoCRTRCA

/-! M11: all bounded fields of S are assembled for k<=N. Residue data and
CM are explicit antecedents. This module does not postulate uniform codes.
The M10 unbounded existential invariant is kept intact. -/
namespace MatematicaAbierta.Continuo.PasoEstadoCRTRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA TrazasInduccionRCA
open DivisionInternaRCA DiferenciasInternasRCA AritmeticaModularInternaRCA
open ProductoAcumuladoRCA InvarianteCRTParcialRCA InversosFuturosRCA
open ActualizacionCodigoCRTRCA
macro "rca_ctx" : term => `(CalculoOrdenRCA.Proof.hypothesis
  (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))

def Γ0 : List Formula := [.le k N,state k p A C,MultiploComunUniformeRCA.cm N b,residueData]
def inverseK : Formula := .exB 54 C (.exB 55 C
  (.conj (.lt (.lit 0) (.var 54))
    (.eq (.mul (.var 54) p) (.add (.lit 1) (.mul (.var 55) n)))))
def atK : Proof Γ0 inverseK := by
  have st : Proof Γ0 (state k p A C) := push hyp
  have ft : Proof Γ0 (future k p b N C) := .andR (.andR (.andR (.andR (.andR st))))
  exact .impE (.allBE 18 (.succ N) k (by decide) ft (.leLtTrans hyp (ltSucc _))) (leRefl k)
def Γq : List Formula := [.exB 55 C (.conj (.lt (.lit 0) q)
  (.eq (.mul q p) (.add (.lit 1) (.mul (.var 55) n)))),.lt q C] ++ Γ0
def Γell : List Formula := [.conj (.lt (.lit 0) q)
  (.eq (.mul q p) (.add (.lit 1) (.mul ell n))),.lt ell C] ++ Γq
def datum : Formula := .exB 17 R (.conj (.member (pair k (.var 17)) 2)
  (.conj (.lt (.var 17) n) (.allB 19 R
    (.imp (.member (pair k (.var 19)) 2) (.eq (.var 17) (.var 19))))))
def datumAtK : Proof Γell datum :=
  .allBE 16 (.succ N) k (by decide) (rca_ctx : Proof Γell residueData)
    (.leLtTrans (rca_ctx : Proof Γell (.le k N)) (ltSucc _))
def Γr : List Formula := [.conj (.member (pair k r) 2)
  (.conj (.lt r n) (.allB 19 R (.imp (.member (pair k (.var 19)) 2) (.eq r (.var 19))))),
  .lt r R] ++ Γell
def rho : Term := .var 72
def h : Term := .var 73
def Γrho : List Formula := [beta A b k rho,.lt rho (.succ A)] ++ Γr
def Γh : List Formula := [.eq A (.add (.mul h n) rho),.lt h (.succ A)] ++ Γrho
def Γd : List Formula := [.eq n (.add rho d),.lt d (.succ n)] ++ Γh
def result : Formula := .exB 75 cap (state (.succ k) nextP (.var 75) cap)

def divisionAtK : Proof Γr (.exB 1 (.succ A) (beta A b k (.var 1))) := by
  have h0 := Proof.allE 8 A (by decide) DivisionBetaRCA.betaTotal
  have h1 := Proof.allE 9 b (by decide) h0
  exact SelectoresInternosRCA.closed (.allE 0 k (by decide) h1)
def complementAtK : Proof Γh (.exB 2 (.succ n) (.eq n (.add rho (.var 2)))) := by
  have read : Proof Γh (beta A b k rho) := rca_ctx
  have bound := Proof.ltLe (.andL read)
  exact .impE (.allBE 1 (.succ n) rho (by decide)
    (SelectoresInternosRCA.closed (.allE 0 n (by decide) boundedDifference))
    (leThenSucc bound)) bound
def betaNew : Proof Γd (beta aNext b k r) := by
  have cert : Proof Γd (.conj (.lt (.lit 0) q)
      (.eq (.mul q p) (.add (.lit 1) (.mul ell n)))) := rca_ctx
  have prescribed : Proof Γd (.conj (.member (pair k r) 2)
      (.conj (.lt r n) (.allB 19 R (.imp (.member (pair k (.var 19)) 2) (.eq r (.var 19)))))) := rca_ctx
  have eqn : Proof Γd (.eq aNext (.add (.mul (quotient h ell d r) n) r)) :=
    updateIdentity A p q ell n h rho d r rca_ctx hyp (.andR cert)
  exact .andI (.andL (.andR prescribed)) (.exBI 12 (.succ aNext) (quotient h ell d r)
    (by decide) (quotientBound aNext _ n r (modulusPositive _ _) eqn) eqn)

def oldPrefix : Proof Γd (readings k aNext b R) := by
  have st : Proof Γd (state k p A C) := rca_ctx
  have fac : Proof Γd (factors k p b) := .andL (.andR (.andR (.andR st)))
  have read : Proof Γd (readings k A b R) := .andL (.andR (.andR (.andR (.andR st))))
  have h0 := Proof.allE 0 N (by decide) prefixClosed
  have h1 := Proof.allE 3 k (by decide) h0
  have h2 := Proof.allE 4 R (by decide) h1
  have h3 := Proof.allE 9 b (by decide) h2
  have h4 := Proof.allE 50 p (by decide) h3
  have h5 := Proof.allE 51 A (by decide) h4
  have h6 := Proof.allE 68 q (by decide) h5
  have h7 := Proof.allE 69 r (by decide) h6
  have h8 := Proof.allE 74 d (by decide) h7
  exact .impE (.impE (SelectoresInternosRCA.closed h8) fac) read
def readPointΓ : List Formula := [
  .member (pair (.var 16) (.var 17)) 2,.lt (.var 17) R,.lt (.var 16) (.succ k)] ++ Γd
def readCases : Proof readPointΓ (beta aNext b (.var 16) (.var 17)) := by
  apply Proof.orderCases (.var 16) k
  · have atI : Proof (.lt (.var 16) k :: readPointΓ)
        (.allB 17 R (.imp (.member (pair (.var 16) (.var 17)) 2)
          (beta aNext b (.var 16) (.var 17)))) :=
      .allBE 16 k (.var 16) (by decide) (push (push (push (push oldPrefix)))) hyp
    exact .impE (.allBE 17 R (.var 17) (by decide) atI (push (push hyp))) (push hyp)
  · have eqIndex : Proof (.eq (.var 16) k :: readPointΓ) (.eq (.var 16) k) := hyp
    have memberK : Proof (.eq (.var 16) k :: readPointΓ) (.member (pair k (.var 17)) 2) :=
      .eqSubst (.member (pair (.var 80) (.var 17)) 2) 80 (.var 16) k
        (by decide) (by decide) eqIndex (push hyp)
    have prescribed : Proof (.eq (.var 16) k :: readPointΓ)
        (.conj (.member (pair k r) 2) (.conj (.lt r n)
          (.allB 19 R (.imp (.member (pair k (.var 19)) 2) (.eq r (.var 19)))))) := rca_ctx
    have equalR : Proof (.eq (.var 16) k :: readPointΓ) (.eq r (.var 17)) :=
      .impE (.allBE 19 R (.var 17) (by decide) (.andR (.andR prescribed)) (push (push hyp))) memberK
    have newR : Proof (.eq (.var 16) k :: readPointΓ) (beta aNext b k (.var 17)) :=
      .eqSubst (beta aNext b k (.var 81)) 81 r (.var 17) (by decide) (by decide) equalR
        (push (push (push (push betaNew))))
    exact .eqSubst (beta aNext b (.var 80) (.var 17)) 80 k (.var 16)
      (by decide) (by decide) (.eqSymm eqIndex) newR
  · exact .botE (.ltIrrefl (.ltLeTrans (push (push (push hyp))) (.ltSuccLe hyp)))
def readingsNext : Proof Γd (readings (.succ k) aNext b R) := by
  apply Proof.allBI 16 (.succ k) (by decide) (by decide)
  apply Proof.allBI 17 R (by decide) (by decide)
  apply Proof.impI
  exact readCases
def stateNext : Proof Γd (state (.succ k) nextP aNext cap) := by
  have st : Proof Γd (state k p A C) := rca_ctx
  have ps : Proof Γd (productState k p b) :=
    .andI (.andL st) (.andL (.andR (.andR (.andR st))))
  have hp0 := Proof.allE 3 k (by decide) productStep
  have hp1 := Proof.allE 9 b (by decide) hp0
  have hp2 := Proof.allE 50 p (by decide) hp1
  have psNext := Proof.impE (SelectoresInternosRCA.closed hp2) ps
  have oldFuture : Proof Γd (future k p b N C) := .andR (.andR (.andR (.andR (.andR st))))
  have hf0 := Proof.allE 0 N (by decide) futureStep
  have hf1 := Proof.allE 9 b (by decide) hf0
  have hf2 := Proof.allE 3 k (by decide) hf1
  have hf3 := Proof.allE 50 p (by decide) hf2
  have hf4 := Proof.allE 52 C (by decide) hf3
  have hf5 := Proof.allE 4 R (by decide) hf4
  have nextFuture : Proof Γd (future (.succ k) nextP b N cap) :=
    .impE (.impE (SelectoresInternosRCA.closed hf5) rca_ctx) oldFuture
  have bound : Proof Γd (.lt aNext cap) :=
    valueBoundFrom (.andL (.andR st)) rca_ctx rca_ctx hyp rca_ctx
  exact .andI (.andL psNext) (.andI bound (.andI capAboveOne
    (.andI (.andR psNext) (.andI readingsNext nextFuture))))

def stateStepOpen : Proof Γ0 result := by
  apply Proof.exBErename 54 68 C (by decide) (by decide) (by decide) (by decide) atK
  apply Proof.exBErename 55 70 C (by decide) (by decide) (by decide) (by decide) hyp
  apply Proof.exBErename 17 69 R (by decide) (by decide) (by decide) (by decide) datumAtK
  apply Proof.exBErename 1 72 (.succ A) (by decide) (by decide) (by decide) (by decide) divisionAtK
  apply Proof.exBErename 12 73 (.succ A) (by decide) (by decide) (by decide) (by decide)
    (.andR (hyp : Proof Γrho _))
  apply Proof.exBErename 2 74 (.succ n) (by decide) (by decide) (by decide) (by decide) complementAtK
  exact .exBI 75 cap aNext (by decide)
    (valueBoundFrom (.andL (.andR (rca_ctx : Proof Γd (state k p A C)))) rca_ctx rca_ctx hyp rca_ctx)
    stateNext
def stateStep : Proof [] ([0,3,4,9,50,51,52].foldr Formula.allN
    (.imp residueData (.imp (MultiploComunUniformeRCA.cm N b)
      (.imp (state k p A C) (.imp (.le k N) result))))) := by
  apply Proof.allI 0 rfl
  apply Proof.allI 3 rfl
  apply Proof.allI 4 rfl
  apply Proof.allI 9 rfl
  apply Proof.allI 50 rfl
  apply Proof.allI 51 rfl
  apply Proof.allI 52 rfl
  exact .impI (.impI (.impI (.impI stateStepOpen)))

example : result.bounded = true := by decide
example : result.numFree.contains 68 = false := by decide
example : result.numFree.contains 69 = false := by decide
example : result.numFree.contains 70 = false := by decide
example : result.numFree.contains 72 = false := by decide
example : result.numFree.contains 73 = false := by decide
example : result.numFree.contains 74 = false := by decide
example : freshNum 68 Γ0 = true := by decide
example : freshNum 69 Γell = true := by decide
example : (Formula.eq A (.add (.mul h n) rho)).safe 73 (.var 12) = true := by decide
#print axioms betaNew
#print axioms readingsNext
#print axioms stateStep
#eval ("new_prescribed_beta_reading", profile betaNew)
#eval ("preserved_and_extended_residue_segment", profile readingsNext)
#eval ("all_bounded_crt_state_fields_step", profile stateStep)
end MatematicaAbierta.Continuo.PasoEstadoCRTRCA
