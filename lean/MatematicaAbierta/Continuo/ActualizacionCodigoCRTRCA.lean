import MatematicaAbierta.Continuo.InversosFuturosRCA

/-! M11/T07. A'=A+P*q*(d+r), from A=h*m+rho, m=rho+d,
q*P=1+ell*m. Exact polynomial identity and preservation of every prefix
reading are internal proof trees. Finite D data remains an antecedent. -/
namespace MatematicaAbierta.Continuo.ActualizacionCodigoCRTRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA TrazasInduccionRCA
open DivisionInternaRCA AritmeticaModularInternaRCA DiferenciasInternasRCA
open ProductoAcumuladoRCA InvarianteCRTParcialRCA InversosFuturosRCA
open CRTConstructivoDosRCA

def value (a p q d r : Term) : Term := .add a (.mul p (.mul q (.add d r)))
def quotient (h ell d r : Term) : Term := .add (.add h (.lit 1)) (.mul ell (.add d r))

def updateIdentity {Γ : List Formula} (a p q ell m h rho d r : Term)
    (ha : Proof Γ (.eq a (.add (.mul h m) rho)))
    (hd : Proof Γ (.eq m (.add rho d)))
    (hi : Proof Γ (.eq (.mul q p) (.add (.lit 1) (.mul ell m)))) :
    Proof Γ (.eq (value a p q d r) (.add (.mul (quotient h ell d r) m) r)) := by
  let dr := Term.add d r
  let t := Term.mul ell dr
  have inc : Proof Γ (.eq (.mul p (.mul q dr)) (.add dr (.mul t m))) :=
    .eqTrans (ax (.trans (.symm (.mulAssoc _ _ _)) (.mul (.mulComm _ _) (.refl _))))
      (.eqTrans (.eqMul hi (eqRefl _)) (ax (.trans (mulRightDistrib _ _ _)
        (.add (mulOneLeft _) (.trans (.mulAssoc _ _ _)
          (.trans (.mul (.refl _) (.mulComm _ _)) (.symm (.mulAssoc _ _ _))))))))
  have group : EqProof (.add (.add (.mul h m) rho) (.add dr (.mul t m)))
      (.add (.add (.mul h m) (.add (.add rho d) r)) (.mul t m)) :=
    .trans (.symm (.addAssoc _ _ _)) (.add
      (.trans (.addAssoc _ _ _) (.add (.refl _) (.symm (.addAssoc _ _ _)))) (.refl _))
  have packet : EqProof (.add (.add (.mul h m) (.add m r)) (.mul t m))
      (.add (.add (.add (.mul h m) m) (.mul t m)) r) :=
    .trans (.add (.symm (.addAssoc _ _ _)) (.refl _)) (shuffle (.add (.mul h m) m) r (.mul t m))
  have expanded : EqProof (.mul (quotient h ell d r) m)
      (.add (.add (.mul h m) m) (.mul t m)) :=
    .trans (mulRightDistrib _ _ _) (.add
      (.trans (mulRightDistrib _ _ _) (.add (.refl _) (mulOneLeft _))) (.refl _))
  exact .eqTrans (.eqAdd ha inc) (.eqTrans (ax group)
    (.eqTrans (.eqAdd (.eqAdd (eqRefl _) (.eqAdd (.eqSymm hd) (eqRefl _))) (eqRefl _))
      (ax (.trans packet (.add (.symm expanded) (.refl _))))))

def q : Term := .var 68
def r : Term := .var 69
def ell : Term := .var 70
def d : Term := .var 74
def aNext : Term := value A p q d r
def carry : Term := .mul q (.add d r)
def prefixΓ : List Formula := [readings k A b R,factors k p b]
def prefixPointΓ : List Formula := [
  .member (pair (.var 16) (.var 17)) 2,.lt (.var 17) R,.lt (.var 16) k] ++ prefixΓ
def prefixPoint : Proof prefixPointΓ (beta aNext b (.var 16) (.var 17)) := by
  have hRead : Proof prefixPointΓ (readings k A b R) := push (push (push (hyp : Proof prefixΓ _)))
  have atI : Proof prefixPointΓ (.allB 17 R
      (.imp (.member (pair (.var 16) (.var 17)) 2) (beta A b (.var 16) (.var 17)))) :=
    .allBE 16 k (.var 16) (by decide) hRead (push (push hyp))
  have old : Proof prefixPointΓ (beta A b (.var 16) (.var 17)) :=
    .impE (.allBE 17 R (.var 17) (by decide) atI (push hyp)) hyp
  have fac : Proof prefixPointΓ (.exB 23 (.succ p)
      (.eq p (.mul (.var 23) (modulus (.var 16) b)))) := by
    have hFac : Proof prefixPointΓ (factors k p b) :=
      push (push (push (push (hyp : Proof [factors k p b] _))))
    have original : Proof prefixPointΓ (.exB 17 (.succ p)
        (.eq p (.mul (.var 17) (modulus (.var 16) b)))) :=
      .allBE 16 k (.var 16) (by decide) hFac (push (push hyp))
    -- Rename the bound name by eliminating and reintroducing it ordinarily.
    apply Proof.exBErename 17 77 (.succ p) (by decide) (by decide) (by decide) (by decide) original
    exact .exBI 23 (.succ p) (.var 77) (by decide) (push hyp) hyp
  have h0 := Proof.allE 8 A (by decide) PreservacionModularBetaRCA.liftBetaClosed
  have h1 := Proof.allE 9 b (by decide) h0
  have h2 := Proof.allE 0 (.var 16) (by decide) h1
  have h3 := Proof.allE 1 (.var 17) (by decide) h2
  have h4 := Proof.allE 30 p (by decide) h3
  have h5 := Proof.allE 31 carry (by decide) h4
  exact .impE (.impE (SelectoresInternosRCA.closed h5) old) fac
def prefixPreserved : Proof prefixΓ (readings k aNext b R) := by
  apply Proof.allBI 16 k (by decide) (by decide)
  apply Proof.allBI 17 R (by decide) (by decide)
  apply Proof.impI
  exact prefixPoint
def prefixClosed : Proof [] ([0,3,4,9,50,51,68,69,74].foldr Formula.allN
    (.imp (factors k p b) (.imp (readings k A b R) (readings k aNext b R)))) :=
  .allI 0 rfl (.allI 3 rfl (.allI 4 rfl (.allI 9 rfl (.allI 50 rfl (.allI 51 rfl
    (.allI 68 rfl (.allI 69 rfl (.allI 74 rfl (.impI (.impI prefixPreserved))))))))))

def identityΓ : List Formula := [
  .eq A (.add (.mul (.var 73) n) (.var 72)),
  .eq n (.add (.var 72) d),.eq (.mul q p) (.add (.lit 1) (.mul ell n))]
def identityConcrete : Proof identityΓ
    (.eq aNext (.add (.mul (quotient (.var 73) ell d r) n) r)) :=
  updateIdentity A p q ell n (.var 73) (.var 72) d r hyp (push hyp) (push (push hyp))
def identityClosed : Proof [] ([3,9,50,51,68,69,70,72,73,74].foldr Formula.allN
    (.imp (.eq (.mul q p) (.add (.lit 1) (.mul ell n)))
      (.imp (.eq n (.add (.var 72) d))
        (.imp (.eq A (.add (.mul (.var 73) n) (.var 72)))
          (.eq aNext (.add (.mul (quotient (.var 73) ell d r) n) r)))))) :=
  by
    apply Proof.allI 3 rfl
    apply Proof.allI 9 rfl
    apply Proof.allI 50 rfl
    apply Proof.allI 51 rfl
    apply Proof.allI 68 rfl
    apply Proof.allI 69 rfl
    apply Proof.allI 70 rfl
    apply Proof.allI 72 rfl
    apply Proof.allI 73 rfl
    apply Proof.allI 74 rfl
    exact .impI (.impI (.impI identityConcrete))

def boundΓ : List Formula := [.lt A C,.lt q C,.lt r R,.eq n (.add (.var 72) d),.le k N]
def valueBoundFrom {Γ : List Formula}
    (hA : Proof Γ (.lt A C)) (hq : Proof Γ (.lt q C)) (hr : Proof Γ (.lt r R))
    (hd : Proof Γ (.eq n (.add (.var 72) d))) (hk : Proof Γ (.le k N)) :
    Proof Γ (.lt aNext cap) := by
  have dLe : Proof Γ (.le d n) :=
    .leRewrite (eqRefl _) (.eqSymm hd) (leLeftAdd d (.var 72))
  have nJ : Proof Γ (.le n J) := modulusMono k N b hk
  have sumBound : Proof Γ (.le (.add d r) (.add J R)) :=
    .leAdd (.leTrans dLe nJ) (.ltLe hr)
  have incBound : Proof Γ (.le (.mul p carry) (.mul p (.mul C (.add J R)))) :=
    leMulLeft p (mulLe (.ltLe hq) sumBound)
  exact .leLtTrans (.leAdd (.ltLe hA) incBound) capAboveU
def valueBound : Proof boundΓ (.lt aNext cap) :=
  valueBoundFrom hyp (push hyp) (push (push hyp)) (push (push (push hyp))) (push (push (push (push hyp))))
def boundClosed : Proof [] ([0,3,4,9,50,51,52,68,69,72,74].foldr Formula.allN
    (.imp (.le k N) (.imp (.eq n (.add (.var 72) d))
      (.imp (.lt r R) (.imp (.lt q C) (.imp (.lt A C) (.lt aNext cap))))))) :=
  by
    apply Proof.allI 0 rfl
    apply Proof.allI 3 rfl
    apply Proof.allI 4 rfl
    apply Proof.allI 9 rfl
    apply Proof.allI 50 rfl
    apply Proof.allI 51 rfl
    apply Proof.allI 52 rfl
    apply Proof.allI 68 rfl
    apply Proof.allI 69 rfl
    apply Proof.allI 72 rfl
    apply Proof.allI 74 rfl
    exact .impI (.impI (.impI (.impI (.impI valueBound))))

example : (readings k aNext b R).bounded = true := by decide
example : (readings k aNext b R).numFree.contains 77 = false := by decide
example : freshNum 77 prefixPointΓ = true := by decide
example : cap.vars.contains 68 = false := by decide
example : cap.vars.contains 69 = false := by decide
example : cap.vars.contains 72 = false := by decide
example : cap.vars.contains 73 = false := by decide
example : cap.vars.contains 74 = false := by decide
#print axioms updateIdentity
#print axioms identityClosed
#print axioms prefixClosed
#print axioms boundClosed
#eval ("crt_update_polynomial_identity", profile identityClosed)
#eval ("crt_update_prefix_preserved", profile prefixClosed)
#eval ("crt_update_uniform_bound", profile boundClosed)
end MatematicaAbierta.Continuo.ActualizacionCodigoCRTRCA
