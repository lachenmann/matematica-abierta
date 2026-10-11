import MatematicaAbierta.Continuo.ProductoAcumuladoRCA

/-! M10/C10: product/new-modulus compatibility follows from effective
inverse certificates, not from a primitive coprimality assertion.
The M09 uniform parameter is used to make positive gap quotients explicit. -/
namespace MatematicaAbierta.Continuo.CompatibilidadProductoRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA DiferenciasInternasRCA
open InversosProductoRCA CoprimalidadPositivaRCA ParametroUniformeBetaRCA MultiploComunUniformeRCA

def positiveFactor {Γ : List Formula} (n d c : Term)
    (hn : Proof Γ (.lt (.lit 0) n)) (he : Proof Γ (.eq n (.mul d c))) :
    Proof Γ (.lt (.lit 0) c) := by
  apply Proof.orderCases (.lit 0) c
  · exact hyp
  · have hz : Proof (.eq (.lit 0) c :: Γ) (.eq n (.lit 0)) :=
      .eqTrans (push he) (.eqTrans (.eqMul (eqRefl _) (.eqSymm hyp)) (ax (.mulZero _)))
    exact .botE (.ltIrrefl (.ltRewrite (eqRefl _) hz (push hn)))
  · exact .botE (.ltIrrefl (.ltLeTrans hyp (.zeroLe _)))

def posGap : Formula := .exB 2 (.succ K)
  (.conj (.eq (.var 21) (.add (.var 20) (.var 2)))
    (.conj (.lt (.lit 0) (.var 2))
      (.exB 17 (.succ B) (.conj (.lt (.lit 0) (.var 17)) (.eq B (.mul (.var 2) (.var 17)))))))

def posGapOpen : Proof pairΓ posGap := by
  apply Proof.exBErename 2 26 (.succ K) (by decide) (by decide) (by decide) (by decide) differenceOpen
  have old : Proof (Formula.conj (.eq (.var 21) (.add (.var 20) (.var 26)))
      (.conj (.lt (.lit 0) (.var 26)) (.exB 17 (.succ B) (.eq B (.mul (.var 26) (.var 17))))) ::
      .lt (.var 26) (.succ K) :: pairΓ)
      (.exB 17 (.succ B) (.eq B (.mul (.var 26) (.var 17)))) := .andR (.andR hyp)
  apply Proof.exBErename 17 31 (.succ B) (by decide) (by decide) (by decide) (by decide) old
  have bPos : Proof (Formula.eq B (.mul (.var 26) (.var 31)) ::
      .lt (.var 31) (.succ B) ::
      Formula.conj (.eq (.var 21) (.add (.var 20) (.var 26)))
        (.conj (.lt (.lit 0) (.var 26)) (.exB 17 (.succ B) (.eq B (.mul (.var 26) (.var 17))))) ::
      .lt (.var 26) (.succ K) :: pairΓ) (.lt (.lit 0) B) :=
    .andL (push (push (push (push (push (push hyp))))))
  apply Proof.exBI 2 (.succ K) (.var 26) (by decide) (push (push (push hyp)))
  apply Proof.andI (.andL (push (push hyp)))
  apply Proof.andI (.andL (.andR (push (push hyp))))
  exact .exBI 17 (.succ B) (.var 31) (by decide) (push hyp)
    (.andI (positiveFactor B (.var 26) (.var 31) bPos hyp) hyp)

def positiveDifferences : Proof [] ([3,40,20,21].foldr Formula.allN
    (.imp (cm K B) (.imp (.lt (.var 20) (.var 21)) (.imp (.le (.var 21) K) posGap)))) :=
  .allI 3 rfl (.allI 40 rfl (.allI 20 rfl (.allI 21 rfl (.impI (.impI (.impI posGapOpen))))))

def P : Term := .var 40
def m : Term := .var 41
def n : Term := .var 42
def a : Term := .var 44
def b : Term := .var 45
def u : Term := .var 46
def v : Term := .var 47
def product : Term := .mul P m
def coefficient : Term := productCoefficient u v n
def leftCert : Formula := .eq (.mul a P) (.add (.lit 1) (.mul u n))
def rightCert : Formula := .eq (.mul b m) (.add (.lit 1) (.mul v n))
def compatΓ : List Formula := [leftCert,rightCert,.lt (.lit 0) n]
def compatResult : Formula :=
  let f := swapConclusion.subst 20 n
  let f := f.subst 21 product
  let f := f.subst 22 (.mul a b)
  f.subst 23 coefficient

def compatibilityOpen : Proof compatΓ compatResult := by
  have eqProduct : Proof compatΓ (.eq (.mul (.mul a b) product)
      (.add (.lit 1) (.mul coefficient n))) := combineInverse P m n a b u v hyp (push hyp)
  have h0 := Proof.allE 20 n (by decide) swapClosed
  have h1 := Proof.allE 21 product (by decide) h0
  have h2 := Proof.allE 22 (.mul a b) (by decide) h1
  have h3 := Proof.allE 23 coefficient (by decide) h2
  exact .impE (.impE (SelectoresInternosRCA.closed h3) (push (push hyp))) eqProduct

def compatibilityClosed : Proof [] ([40,41,42,44,45,46,47].foldr Formula.allN
    (.imp (.lt (.lit 0) n) (.imp rightCert (.imp leftCert compatResult)))) := by
  apply Proof.allI 40 rfl
  apply Proof.allI 41 rfl
  apply Proof.allI 42 rfl
  apply Proof.allI 44 rfl
  apply Proof.allI 45 rfl
  apply Proof.allI 46 rfl
  apply Proof.allI 47 rfl
  exact .impI (.impI (.impI compatibilityOpen))

def productCommonDivisorOne {Γ : List Formula} (p m n a b u v g s t : Term)
    (hp : Proof Γ (.eq (.mul a p) (.add (.lit 1) (.mul u n))))
    (hm : Proof Γ (.eq (.mul b m) (.add (.lit 1) (.mul v n))))
    (hn : Proof Γ (.eq n (.mul g s)))
    (hprod : Proof Γ (.eq (.mul p m) (.mul g t)))
    (hg : Proof Γ (.lt (.lit 0) g)) : Proof Γ (.eq g (.lit 1)) :=
  commonDivisorOne (.mul a b) (productCoefficient u v n) n (.mul p m) g s t
    (combineInverse p m n a b u v hp hm) hn hprod hg

example : posGap.bounded = true := by decide
example : posGap.numFree.contains 26 = false := by decide
example : posGap.numFree.contains 31 = false := by decide
example : compatResult.bounded = true := by decide
example : compatResult.numFree.contains 34 = false := by decide
example : freshNum 34 compatΓ = true := by decide
#print axioms positiveFactor
#print axioms positiveDifferences
#print axioms compatibilityClosed
#print axioms productCommonDivisorOne
#eval ("positive_uniform_gap_certificates", profile positiveDifferences)
#eval ("new_modulus_product_compatibility", profile compatibilityClosed)
end MatematicaAbierta.Continuo.CompatibilidadProductoRCA
