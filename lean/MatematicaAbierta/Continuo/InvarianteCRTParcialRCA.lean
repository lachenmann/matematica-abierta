import MatematicaAbierta.Continuo.CompatibilidadProductoRCA

/-! M10/C10: explicit Sigma1 partial-CRT invariant and effective empty-prefix
base. The full induction STEP and uniform fixed-b CRT have NO Proof here.
Finite residue data is a bounded antecedent; its existence is not assumed. -/
namespace MatematicaAbierta.Continuo.InvarianteCRTParcialRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA TrazasInduccionRCA
open ProductoAcumuladoRCA
abbrev EProof := CalculoExistencialRCA.Proof
def N : Term := .var 0
def R : Term := .var 4
def A : Term := .var 51
def C : Term := .var 52

def readings (count code param bound : Term) : Formula :=
  .allB 16 count (.allB 17 bound
    (.imp (.member (pair (.var 16) (.var 17)) 2)
      (beta code param (.var 16) (.var 17))))
def future (count product param limit cap : Term) : Formula :=
  .allB 18 (.succ limit) (.imp (.le count (.var 18))
    (.exB 54 cap (.exB 55 cap
      (.conj (.lt (.lit 0) (.var 54))
        (.eq (.mul (.var 54) product)
          (.add (.lit 1) (.mul (.var 55) (modulus (.var 18) param))))))))
def state (count product code cap : Term) : Formula :=
  .conj (.lt (.lit 0) product) (.conj (.lt code cap) (.conj (.lt (.lit 1) cap)
    (.conj (factors count product b)
      (.conj (readings count code b R) (future count product b N cap)))))
def matrix : Formula := .imp (.le k (.succ N)) (state k p A C)
def invariant : Formula := .exN 50 (.exN 51 (.exN 52 matrix))
def invariantSigma1 : Sigma1 invariant :=
  .exists 50 (.exists 51 (.exists 52 (.bounded (by decide))))

/-- Bounded relation of prescribed residues. D, set variable 2, is explicit;
totality, unique values and residue bounds are antecedents, not axioms. -/
def residueData : Formula := .allB 16 (.succ N) (.exB 17 R
  (.conj (.member (pair (.var 16) (.var 17)) 2)
    (.conj (.lt (.var 17) (modulus (.var 16) b))
      (.allB 19 R (.imp (.member (pair (.var 16) (.var 19)) 2)
        (.eq (.var 17) (.var 19)))))))
def fixedBCRTGoal : Formula := [0,4,9].foldr Formula.allN
  (.imp (MultiploComunUniformeRCA.cm N b)
    (.imp residueData (.exN 51 (readings (.succ N) A b R))))
def fullStepGoal : Formula := .allN 3 (.imp invariant (invariant.subst 3 (.succ k)))

def emptyReadings : Proof [] (readings (.lit 0) (.lit 0) b R) := by
  apply Proof.allBI 16 (.lit 0) rfl rfl
  exact .botE (.ltIrrefl (.ltLeTrans hyp (.zeroLe _)))

def emptyFuture : Proof [] (future (.lit 0) (.lit 1) b N (.lit 2)) := by
  apply Proof.allBI 18 (.succ N) rfl rfl
  apply Proof.impI
  apply Proof.exBI 54 (.lit 2) (.lit 1) (by decide) (.embed ConstruccionBaseTrazaRCA.oneLtTwo)
  apply Proof.exBI 55 (.lit 2) (.lit 0) (by decide)
    (.leLtTrans (.zeroLe (.lit 1)) (.embed ConstruccionBaseTrazaRCA.oneLtTwo))
  apply Proof.andI (.embed ConstruccionBaseTrazaRCA.zeroLtOne)
  exact ax (.trans (numeralMul 1 1) (.symm (.trans
    (.add (.refl _) (ConstruccionBaseTrazaRCA.zeroProduct _)) (.addZero _))))

def baseState : Proof [] (state (.lit 0) (.lit 1) (.lit 0) (.lit 2)) :=
  .andI (.embed ConstruccionBaseTrazaRCA.zeroLtOne)
    (.andI (.leLtTrans (.zeroLe (.lit 1)) (.embed ConstruccionBaseTrazaRCA.oneLtTwo))
      (.andI (.embed ConstruccionBaseTrazaRCA.oneLtTwo)
        (.andI (.andR productBaseMatrix) (.andI emptyReadings emptyFuture))))

def base : EProof [] (invariant.subst 3 (.lit 0)) := by
  apply CalculoExistencialRCA.Proof.exNI 50 (.lit 1) (by decide)
  apply CalculoExistencialRCA.Proof.exNI 51 (.lit 0) (by decide)
  apply CalculoExistencialRCA.Proof.exNI 52 (.lit 2) (by decide)
  apply CalculoExistencialRCA.Proof.impI
  exact .embed (push baseState)

def baseClosed : EProof [] ([0,4,9].foldr Formula.allN (invariant.subst 3 (.lit 0))) :=
  .allI 0 rfl (.allI 4 rfl (.allI 9 rfl base))

example : matrix.bounded = true := by decide
example : residueData.bounded = true := by decide
example : invariant.safe 3 (.succ k) = true := by decide
example : freshNum 3 [MultiploComunUniformeRCA.cm N b,residueData] = true := by decide
example : invariant.numFree.contains 50 = false := by decide
example : invariant.numFree.contains 51 = false := by decide
example : invariant.numFree.contains 52 = false := by decide
example : fixedBCRTGoal.numFree = [] := by decide
example : invariant.setFree = [2] := by decide
#print axioms invariantSigma1
#print axioms baseState
#print axioms baseClosed
#eval ("partial_crt_empty_prefix_base", CalculoExistencialRCA.profile baseClosed)
end MatematicaAbierta.Continuo.InvarianteCRTParcialRCA
