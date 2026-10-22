import MatematicaAbierta.Continuo.ParametroUniformeBetaRCA

/-! M10/C10: positive inverse certificates are multiplied explicitly.
No pairwise-coprime-to-product rule, Bezout or CRT axiom is used. -/
namespace MatematicaAbierta.Continuo.InversosProductoRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA DiferenciasInternasRCA
open CRTConstructivoDosRCA CoprimalidadPositivaRCA AritmeticaModularInternaRCA

def productCoefficient (a b n : Term) : Term :=
  .add (.add a b) (.mul (.mul a b) n)

def productRegroup (a b p m : Term) : EqProof
    (.mul (.mul a b) (.mul p m)) (.mul (.mul a p) (.mul b m)) :=
  .trans (.mulAssoc _ _ _) (.trans (.mul (.refl _)
    (.trans (.symm (.mulAssoc _ _ _)) (.trans (.mul (.mulComm _ _) (.refl _)) (.mulAssoc _ _ _))))
      (.symm (.mulAssoc _ _ _)))

def productPacket (a b n : Term) : EqProof
    (.mul (.add (.lit 1) (.mul a n)) (.add (.lit 1) (.mul b n)))
    (.add (.lit 1) (.mul (productCoefficient a b n) n)) := by
  have left : EqProof
      (.mul (.add (.lit 1) (.mul a n)) (.add (.lit 1) (.mul b n)))
      (.add (.lit 1) (.add (.mul a n) (.add (.mul b n) (.mul (.mul a n) (.mul b n))))) :=
    .trans (.distrib _ _ _)
      (.trans (.add (mulOneRight _) (.trans (mulRightDistrib _ _ _) (.add (mulOneLeft _) (.refl _))))
        (.addAssoc _ _ _))
  have cross : EqProof (.mul (.mul a n) (.mul b n)) (.mul (.mul (.mul a b) n) n) :=
    .trans (.symm (productRegroup a b n n)) (.symm (.mulAssoc _ _ _))
  have right : EqProof (.add (.lit 1) (.mul (productCoefficient a b n) n))
      (.add (.lit 1) (.add (.mul a n) (.add (.mul b n) (.mul (.mul a n) (.mul b n))))) :=
    .add (.refl _) (.trans (mulRightDistrib _ _ _)
      (.trans (.add (mulRightDistrib _ _ _) (.symm cross)) (.addAssoc _ _ _)))
  exact .trans left (.symm right)

def combineInverse {Γ : List Formula} (p m n a b u v : Term)
    (hp : Proof Γ (.eq (.mul a p) (.add (.lit 1) (.mul u n))))
    (hm : Proof Γ (.eq (.mul b m) (.add (.lit 1) (.mul v n)))) :
    Proof Γ (.eq (.mul (.mul a b) (.mul p m))
      (.add (.lit 1) (.mul (productCoefficient u v n) n))) :=
  .eqTrans (ax (productRegroup a b p m)) (.eqTrans (.eqMul hp hm) (ax (productPacket u v n)))

def swappedEquality {Γ : List Formula} (m n q ell z : Term)
    (hi : Proof Γ (.eq (.mul q n) (.add (.lit 1) (.mul ell m))))
    (hz : Proof Γ (.eq m (.add (.lit 1) z))) :
    Proof Γ (.eq (.mul (.add (.lit 1) (.mul ell z)) m)
      (.add (.lit 1) (.mul (.mul z q) n))) := by
  have rearrange : EqProof (.mul (.mul ell z) m) (.mul z (.mul ell m)) :=
    .trans (.mul (.mulComm _ _) (.refl _)) (.mulAssoc _ _ _)
  have packet : EqProof (.add (.lit 1) (.mul z (.add (.lit 1) (.mul ell m))))
      (.add (.add (.lit 1) z) (.mul z (.mul ell m))) :=
    .trans (.add (.refl _) (.distrib _ _ _))
      (.trans (.add (.refl _) (.add (mulOneRight z) (.refl _))) (.symm (.addAssoc _ _ _)))
  exact .eqTrans (ax (.trans (mulRightDistrib _ _ _) (.add (mulOneLeft m) rearrange)))
    (.eqTrans (.eqAdd hz (eqRefl _)) (.eqTrans (ax (.symm packet))
      (.eqTrans (.eqAdd (eqRefl _) (.eqMul (eqRefl z) (.eqSymm hi)))
        (ax (.add (.refl _) (.symm (.mulAssoc _ _ _)))))))

def swapContext : List Formula := [.eq (.mul (.var 22) (.var 21))
  (.add (.lit 1) (.mul (.var 23) (.var 20))), .lt (.lit 0) (.var 20)]
def swapConclusion : Formula := .exB 32 (.succ (.add (.lit 1) (.mul (.var 23) (.var 20))))
  (.exB 33 (.succ (.mul (.var 20) (.var 22)))
    (.conj (.lt (.lit 0) (.var 32))
      (.eq (.mul (.var 32) (.var 20)) (.add (.lit 1) (.mul (.var 33) (.var 21))))))

def swapOpen : Proof swapContext swapConclusion := by
  have oneLe : Proof swapContext (.le (.lit 1) (.var 20)) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe (push hyp))
  have predecessor : Proof swapContext (.exB 2 (.succ (.var 20))
      (.eq (.var 20) (.add (.lit 1) (.var 2)))) :=
    .impE (.allBE 1 (.succ (.var 20)) (.lit 1) (by decide)
      (SelectoresInternosRCA.closed (.allE 0 (.var 20) (by decide) boundedDifference))
      (leThenSucc oneLe)) oneLe
  apply Proof.exBErename 2 34 (.succ (.var 20)) (by decide) (by decide) (by decide) (by decide) predecessor
  have zLe : Proof ([Formula.eq (.var 20) (.add (.lit 1) (.var 34)),
      .lt (.var 34) (.succ (.var 20))] ++ swapContext) (.le (.var 34) (.var 20)) :=
    .leRewrite (eqRefl _) (.eqSymm hyp) (leLeftAdd (.var 34) (.lit 1))
  apply Proof.exBI 32 (.succ (.add (.lit 1) (.mul (.var 23) (.var 20))))
    (.add (.lit 1) (.mul (.var 23) (.var 34))) (by decide)
    (leThenSucc (leAddLeft (.lit 1) (leMulLeft (.var 23) zLe)))
  apply Proof.exBI 33 (.succ (.mul (.var 20) (.var 22))) (.mul (.var 34) (.var 22)) (by decide)
    (leThenSucc (.leMulRight (.var 22) zLe))
  exact .andI (.leLtTrans (.zeroLe _) (oneAddPositive _))
    (swappedEquality (.var 20) (.var 21) (.var 22) (.var 23) (.var 34) (push (push hyp)) hyp)

def swapClosed : Proof [] ([20,21,22,23].foldr Formula.allN
    (.imp (.lt (.lit 0) (.var 20)) (.imp (.eq (.mul (.var 22) (.var 21))
      (.add (.lit 1) (.mul (.var 23) (.var 20)))) swapConclusion))) :=
  .allI 20 rfl (.allI 21 rfl (.allI 22 rfl (.allI 23 rfl (.impI (.impI swapOpen)))))

def combineContext : List Formula := [
  .eq (.mul (.var 24) (.var 20)) (.add (.lit 1) (.mul (.var 26) (.var 22))),
  .eq (.mul (.var 25) (.var 21)) (.add (.lit 1) (.mul (.var 27) (.var 22))),
  .lt (.lit 0) (.var 24), .lt (.lit 0) (.var 25)]
def combineConclusion : Formula := .conj (.lt (.lit 0) (.mul (.var 24) (.var 25)))
  (.eq (.mul (.mul (.var 24) (.var 25)) (.mul (.var 20) (.var 21)))
    (.add (.lit 1) (.mul (productCoefficient (.var 26) (.var 27) (.var 22)) (.var 22))))
def combineClosed : Proof [] ([20,21,22,24,25,26,27].foldr Formula.allN
    (.imp (.lt (.lit 0) (.var 25)) (.imp (.lt (.lit 0) (.var 24))
      (.imp (.eq (.mul (.var 25) (.var 21)) (.add (.lit 1) (.mul (.var 27) (.var 22))))
        (.imp (.eq (.mul (.var 24) (.var 20)) (.add (.lit 1) (.mul (.var 26) (.var 22))))
          combineConclusion))))) := by
  apply Proof.allI 20 rfl
  apply Proof.allI 21 rfl
  apply Proof.allI 22 rfl
  apply Proof.allI 24 rfl
  apply Proof.allI 25 rfl
  apply Proof.allI 26 rfl
  apply Proof.allI 27 rfl
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  exact .andI (positiveProduct (.var 24) (.var 25) (push (push hyp)) (push (push (push hyp))))
    (combineInverse (.var 20) (.var 21) (.var 22) (.var 24) (.var 25) (.var 26) (.var 27) hyp (push hyp))

example : swapConclusion.bounded = true := by decide
example : swapConclusion.numFree.contains 34 = false := by decide
example : swapConclusion.safe 22 (.var 35) = true := by decide
example : combineConclusion.bounded = true := by decide
#print axioms productPacket
#print axioms combineInverse
#print axioms swapClosed
#print axioms combineClosed
#eval ("swap_positive_inverse", profile swapClosed)
#eval ("product_inverse_certificate", profile combineClosed)
end MatematicaAbierta.Continuo.InversosProductoRCA
