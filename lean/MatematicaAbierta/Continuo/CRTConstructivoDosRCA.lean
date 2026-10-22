import MatematicaAbierta.Continuo.IdentidadModulosBetaRCA

/-! M08 C09: constructive two-modulus CRT from a POSITIVE inverse
certificate q*n=1+ell*m. The certificate is an explicit antecedent here;
IdentidadModulosBetaRCA derives it for the special moduli. All complements,
quotients and bounds below are internally constructed, not rules/axioms. -/
namespace MatematicaAbierta.Continuo.CRTConstructivoDosRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA LecturasBetaRCA
open DiferenciasInternasRCA AritmeticaModularInternaRCA

def swapFactors (a b c : Term) : EqProof (.mul (.mul a b) c) (.mul b (.mul a c)) :=
  .trans (.mul (.mulComm _ _) (.refl _)) (.mulAssoc _ _ _)
def mulOneRight (t : Term) : EqProof (.mul t (.lit 1)) t :=
  .trans (.mulComm _ _) (mulOneLeft t)
def crtValue (r d ell m : Term) : Term := .add r (.mul (.mul ell (.add r d)) m)

def crtSecondEquality {Γ : List Formula} (r s d ell m n q y : Term)
    (hi : Proof Γ (.eq (.mul q n) (.add (.lit 1) (.mul ell m))))
    (hd : Proof Γ (.eq n (.add s d)))
    (hy : Proof Γ (.eq (.mul (.add r d) q) (.add (.lit 1) y))) :
    Proof Γ (.eq (crtValue r d ell m) (.add (.mul y n) s)) := by
  let rd := Term.add r d
  let x := crtValue r d ell m
  have hleft : EqProof (.add x d) (.mul rd (.add (.lit 1) (.mul ell m))) :=
    .trans (shuffle r (.mul (.mul ell rd) m) d)
      (.trans (.add (.refl _) (swapFactors ell rd m))
        (.trans (.add (.symm (mulOneRight rd)) (.refl _)) (.symm (.distrib _ _ _))))
  have hright : EqProof (.add (.add s d) (.mul y n)) (.add (.add (.mul y n) s) d) :=
    .trans (shuffle s d (.mul y n)) (.add (.addComm _ _) (.refl _))
  have he : Proof Γ (.eq (.add x d) (.add (.add (.mul y n) s) d)) :=
    .eqTrans (ax hleft) (.eqTrans (.eqMul (eqRefl rd) (.eqSymm hi))
      (.eqTrans (ax (.symm (.mulAssoc _ _ _))) (.eqTrans (.eqMul hy (eqRefl n))
        (.eqTrans (ax (.trans (mulRightDistrib (.lit 1) y n) (.add (mulOneLeft n) (.refl _))))
          (.eqTrans (.eqAdd hd (eqRefl _)) (ax hright))))))
  exact .addCancelLeft d (.eqTrans (ax (.addComm d x))
    (.eqTrans he (ax (.addComm (.add (.mul y n) s) d))))

def residue (x m r : Term) : Formula := .conj (.lt r m)
  (.exB 12 (.succ x) (.eq x (.add (.mul (.var 12) m) r)))
def upper (ell : Term) : Term :=
  .add (.var 24) (.mul (.mul ell (.add (.var 24) (.var 21))) (.var 20))
def crtConclusion : Formula := .exB 28 (.succ (upper (.var 23)))
  (.conj (residue (.var 28) (.var 20) (.var 24)) (residue (.var 28) (.var 21) (.var 25)))
def crtContext : List Formula :=
  [.eq (.mul (.var 22) (.var 21)) (.add (.lit 1) (.mul (.var 23) (.var 20))),
   .lt (.var 24) (.var 20), .lt (.var 25) (.var 21),
   .lt (.lit 0) (.var 22), .lt (.lit 0) (.var 21), .lt (.lit 0) (.var 20)]
def complement : Formula := .exB 2 (.succ (.var 21))
  (.eq (.var 21) (.add (.var 25) (.var 2)))

def complementExists : Proof crtContext complement :=
  .impE (.allBE 1 (.succ (.var 21)) (.var 25) (by decide)
    (SelectoresInternosRCA.closed (.allE 0 (.var 21) (by decide) boundedDifference))
    (leThenSucc (.ltLe (push (push hyp))))) (.ltLe (push (push hyp)))

def dContext : List Formula :=
  [.eq (.var 21) (.add (.var 25) (.var 26)), .lt (.var 26) (.succ (.var 21))] ++ crtContext
def pTerm : Term := .mul (.add (.var 24) (.var 26)) (.var 22)
def pPositive : Proof dContext (.lt (.lit 0) pTerm) :=
  positiveProduct (.add (.var 24) (.var 26)) (.var 22)
    (.ltLeTrans (positiveComplement (.var 25) (.var 26) (.var 21)
      (push (push (push (push hyp)))) hyp) (leLeftAdd (.var 26) (.var 24)))
    (push (push (push (push (push hyp)))))

def pPredecessor : Proof dContext
    (.exB 2 (.succ pTerm) (.eq pTerm (.add (.lit 1) (.var 2)))) := by
  have hone : Proof dContext (.le (.lit 1) pTerm) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe pPositive)
  exact .impE (.allBE 1 (.succ pTerm) (.lit 1) (by decide)
    (SelectoresInternosRCA.closed (.allE 0 pTerm (by decide) boundedDifference))
    (leThenSucc hone)) hone

def yContext : List Formula :=
  [.eq pTerm (.add (.lit 1) (.var 27)), .lt (.var 27) (.succ pTerm)] ++ dContext
def xTerm : Term := crtValue (.var 24) (.var 26) (.var 23) (.var 20)

def crtWitness : Proof yContext crtConclusion := by
  have hd : Proof yContext (.eq (.var 21) (.add (.var 25) (.var 26))) := push (push hyp)
  have hi : Proof yContext
      (.eq (.mul (.var 22) (.var 21)) (.add (.lit 1) (.mul (.var 23) (.var 20)))) :=
    push (push (push (push hyp)))
  have hm : Proof yContext (.lt (.lit 0) (.var 20)) :=
    push (push (push (push (push (push (push (push (push hyp))))))))
  have hn : Proof yContext (.lt (.lit 0) (.var 21)) :=
    push (push (push (push (push (push (push (push hyp)))))))
  have hr : Proof yContext (.lt (.var 24) (.var 20)) :=
    push (push (push (push (push hyp))))
  have hs : Proof yContext (.lt (.var 25) (.var 21)) :=
    push (push (push (push (push (push hyp)))))
  have dLe : Proof yContext (.le (.var 26) (.var 21)) :=
    .leRewrite (eqRefl _) (.eqSymm hd) (leLeftAdd (.var 26) (.var 25))
  have hxBound : Proof yContext (.lt xTerm (.succ (upper (.var 23)))) :=
    leThenSucc (leAddLeft (.var 24) (.leMulRight (.var 20)
      (leMulLeft (.var 23) (leAddLeft (.var 24) dLe))))
  have he₁ : Proof yContext (.eq xTerm
      (.add (.mul (.mul (.var 23) (.add (.var 24) (.var 26))) (.var 20)) (.var 24))) :=
    ax (.addComm _ _)
  have he₂ : Proof yContext (.eq xTerm (.add (.mul (.var 27) (.var 21)) (.var 25))) :=
    crtSecondEquality (.var 24) (.var 25) (.var 26) (.var 23) (.var 20) (.var 21) (.var 22) (.var 27)
      hi hd hyp
  apply Proof.exBI 28 (.succ (upper (.var 23))) xTerm (by decide) hxBound
  apply Proof.andI
  · apply Proof.andI hr
    apply Proof.exBI 12 (.succ xTerm) (.mul (.var 23) (.add (.var 24) (.var 26)))
      (by decide) (quotientBound xTerm _ (.var 20) (.var 24) hm he₁)
    exact he₁
  · apply Proof.andI hs
    apply Proof.exBI 12 (.succ xTerm) (.var 27) (by decide)
      (quotientBound xTerm (.var 27) (.var 21) (.var 25) hn he₂)
    exact he₂

def crtOpen : Proof crtContext crtConclusion := by
  apply Proof.exBErename 2 26 (.succ (.var 21)) (by decide) (by decide) (by decide)
    (by decide) complementExists
  apply Proof.exBErename 2 27 (.succ pTerm) (by decide) (by decide) (by decide)
    (by decide) pPredecessor
  exact crtWitness

def crtTwo : Proof []
    (.allN 20 (.allN 21 (.allN 22 (.allN 23 (.allN 24 (.allN 25
      (.imp (.lt (.lit 0) (.var 20)) (.imp (.lt (.lit 0) (.var 21))
       (.imp (.lt (.lit 0) (.var 22)) (.imp (.lt (.var 25) (.var 21))
        (.imp (.lt (.var 24) (.var 20))
         (.imp (.eq (.mul (.var 22) (.var 21)) (.add (.lit 1) (.mul (.var 23) (.var 20))))
           crtConclusion)))))))))))) :=
  .allI 20 rfl (.allI 21 rfl (.allI 22 rfl (.allI 23 rfl (.allI 24 rfl (.allI 25 rfl
    (.impI (.impI (.impI (.impI (.impI (.impI crtOpen)))))))))))

example : crtConclusion.bounded = true := by decide
example : crtConclusion.numFree.contains 26 = false := by decide
example : crtConclusion.numFree.contains 27 = false := by decide
example : crtConclusion.safe 23 (.var 29) = true := by decide
#print axioms crtSecondEquality
#print axioms crtWitness
#print axioms crtTwo
#eval ("crt_two_positive_certificate", profile crtTwo)
end MatematicaAbierta.Continuo.CRTConstructivoDosRCA
