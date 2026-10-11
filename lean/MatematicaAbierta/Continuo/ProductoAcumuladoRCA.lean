import MatematicaAbierta.Continuo.InversosProductoRCA

/-! M10/C10: internally certified product extension P'=P*m_k, with
bounded quotients for every prior factor and the new factor. No uniform
beta code for the product history is asserted. -/
namespace MatematicaAbierta.Continuo.ProductoAcumuladoRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA DiferenciasInternasRCA
open MultiploComunUniformeRCA InversosProductoRCA
def k : Term := .var 3
def b : Term := .var 9
def p : Term := .var 50
def n : Term := modulus k b
def nextP : Term := .mul p n
def factors (count product param : Term) : Formula :=
  .allB 16 count (.exB 17 (.succ product)
    (.eq product (.mul (.var 17) (modulus (.var 16) param))))
def productState (count product param : Term) : Formula :=
  .conj (.lt (.lit 0) product) (factors count product param)
def stepΓ : List Formula := [.lt (.var 16) (.succ k), productState k p b]
def factorConclusion : Formula := .exB 17 (.succ nextP)
  (.eq nextP (.mul (.var 17) (modulus (.var 16) b)))

def factorCases : Proof stepΓ factorConclusion := by
  apply Proof.orderCases (.var 16) k
  · have old : Proof (.lt (.var 16) k :: stepΓ)
        (.exB 17 (.succ p) (.eq p (.mul (.var 17) (modulus (.var 16) b)))) :=
      .allBE 16 k (.var 16) (by decide) (.andR (push (push hyp))) hyp
    apply Proof.exBErename 17 31 (.succ p) (by decide) (by decide) (by decide) (by decide) old
    have he : Proof (Formula.eq p (.mul (.var 31) (modulus (.var 16) b)) ::
        .lt (.var 31) (.succ p) :: .lt (.var 16) k :: stepΓ)
        (.eq nextP (.mul (.mul (.var 31) n) (modulus (.var 16) b))) :=
      .eqTrans (.eqMul hyp (eqRefl _)) (ax (.trans (.mulAssoc _ _ _)
        (.trans (.mul (.refl _) (.mulComm _ _)) (.symm (.mulAssoc _ _ _)))))
    apply Proof.exBI 17 (.succ nextP) (.mul (.var 31) n) (by decide)
    · exact factorBound nextP (modulus (.var 16) b) (.mul (.var 31) n)
        (modulusPositive _ _) (.eqTrans he (ax (.mulComm _ _)))
    · exact he
  · have hm : Proof (.eq (.var 16) k :: stepΓ) (.eq (modulus (.var 16) b) n) :=
      .eqAdd (eqRefl _) (.eqMul (.eqAdd hyp (eqRefl _)) (eqRefl _))
    have he : Proof (.eq (.var 16) k :: stepΓ)
        (.eq nextP (.mul p (modulus (.var 16) b))) := .eqMul (eqRefl _) (.eqSymm hm)
    exact .exBI 17 (.succ nextP) p (by decide)
      (factorBound nextP (modulus (.var 16) b) p (modulusPositive _ _) (.eqTrans he (ax (.mulComm _ _)))) he
  · exact .botE (.ltIrrefl (.ltLeTrans (push hyp) (.ltSuccLe hyp)))

def productStepOpen : Proof [productState k p b] (productState (.succ k) nextP b) := by
  apply Proof.andI
  · exact positiveProduct p n (.andL hyp) (modulusPositive _ _)
  · apply Proof.allBI 16 (.succ k) (by decide) (by decide)
    exact factorCases

def productStep : Proof [] ([3,9,50].foldr Formula.allN
    (.imp (productState k p b) (productState (.succ k) nextP b))) :=
  .allI 3 rfl (.allI 9 rfl (.allI 50 rfl (.impI productStepOpen)))

def scalarExists : Formula := .exN 53 (productState (.succ k) (.var 53) b)
def scalarStep : CalculoExistencialRCA.Proof [] ([3,9,50].foldr Formula.allN
    (.imp (productState k p b) scalarExists)) := by
  apply CalculoExistencialRCA.Proof.allI 3 rfl
  apply CalculoExistencialRCA.Proof.allI 9 rfl
  apply CalculoExistencialRCA.Proof.allI 50 rfl
  apply CalculoExistencialRCA.Proof.impI
  apply CalculoExistencialRCA.Proof.exNI 53 nextP (by decide)
  exact .embed productStepOpen

def productExists : Formula := .exN 50 (productState k p b)
def productSigma1 : Sigma1 productExists := .exists 50 (.bounded (by decide))

def productBaseMatrix : Proof [] (productState (.lit 0) (.lit 1) b) := by
  apply Proof.andI (.embed ConstruccionBaseTrazaRCA.zeroLtOne)
  apply Proof.allBI 16 (.lit 0) rfl rfl
  exact .botE (.ltIrrefl (.ltLeTrans hyp (.zeroLe _)))

def productExistenceBase : CalculoExistencialRCA.Proof [] (productExists.subst 3 (.lit 0)) := by
  apply CalculoExistencialRCA.Proof.exNI 50 (.lit 1) (by decide)
  exact .embed productBaseMatrix

def productExistenceStep : CalculoExistencialRCA.Proof []
    (.allN 3 (.imp productExists (productExists.subst 3 (.succ k)))) := by
  apply CalculoExistencialRCA.Proof.allI 3 rfl
  apply CalculoExistencialRCA.Proof.impI
  apply CalculoExistencialRCA.Proof.exNE 50 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNI 50 nextP (by decide)
  exact .embed (.weaken (fun _ hm => by
    cases hm with
    | head => exact List.mem_cons_self
    | tail _ h => cases h) productStepOpen)

/-- Uniform existence of a positive scalar with bounded factor certificates.
The proof chooses P0=1, P'=P*m_k. The formula does NOT certify a beta-coded
history of all products and does NOT assert the finite CRT. -/
def uniformProductCertificates : CalculoExistencialRCA.Proof []
    (.allN 9 (.allN 3 productExists)) :=
  .allI 9 rfl (.sigma1Induction 3 productSigma1 rfl (by decide) (by decide)
    productExistenceBase productExistenceStep)

/-- Two readings for the initial product history P0=1, P1=m0(b).
This AUXILIARY beta-code parameter is different from fixed CRT parameter b.
No arbitrary-length product history is claimed. -/
def initialCodeFormula : Formula :=
  let f := ParametroParBetaRCA.orderedResult.subst 24 (.lit 1)
  let f := f.subst 25 (modulus (.lit 0) b)
  let f := f.subst 0 (.lit 0)
  f.subst 1 (.lit 1)
def initialProductCode : Proof [] (.allN 9 initialCodeFormula) := by
  apply Proof.allI 9 rfl
  have h0 := Proof.allE 24 (.lit 1) (by decide) ParametroParBetaRCA.pairCodeFromOrder
  have h1 := Proof.allE 25 (modulus (.lit 0) b) (by decide) h0
  have h2 := Proof.allE 0 (.lit 0) (by decide) h1
  have h3 := Proof.allE 1 (.lit 1) (by decide) h2
  exact .impE h3 (.embed ConstruccionBaseTrazaRCA.zeroLtOne)

example : (productState k p b).bounded = true := by decide
example : factorConclusion.numFree.contains 31 = false := by decide
example : freshNum 31 stepΓ = true := by decide
example : (productState (.succ k) (.var 53) b).safe 53 nextP = true := by decide
example : initialCodeFormula.bounded = true := by decide
example : (Formula.allN 9 initialCodeFormula).numFree = [] := by decide
example : productExists.safe 3 (.succ k) = true := by decide
example : freshNum 50 [productExists] = true := by decide
example : (productExists.subst 3 (.succ k)).numFree.contains 50 = false := by decide
example : (Formula.allN 9 (.allN 3 productExists)).numFree = [] := by decide
#print axioms productStep
#print axioms scalarStep
#print axioms initialProductCode
#print axioms uniformProductCertificates
#eval ("product_factor_step", profile productStep)
#eval ("product_scalar_exists", CalculoExistencialRCA.profile scalarStep)
#eval ("initial_two_product_codes", profile initialProductCode)
#eval ("uniform_scalar_product_certificates", CalculoExistencialRCA.profile uniformProductCertificates)
end MatematicaAbierta.Continuo.ProductoAcumuladoRCA
