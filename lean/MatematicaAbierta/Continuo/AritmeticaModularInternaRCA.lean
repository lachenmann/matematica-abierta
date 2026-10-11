import MatematicaAbierta.Continuo.DivisionBetaRCA

/-! M07: modular lifting certificates needed by the CRT construction.
Divisibility certificates are ANTECEDENTS, not rules/axioms.
No Bezout, inverse, common multiple or finite CRT existence is asserted. -/
namespace MatematicaAbierta.Continuo.AritmeticaModularInternaRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA

def quotientBound {Γ : List Formula} (a q m r : Term)
    (hm : Proof Γ (.lt (.lit 0) m))
    (he : Proof Γ (.eq a (.add (.mul q m) r))) : Proof Γ (.lt q (.succ a)) := by
  have hOne : Proof Γ (.le (.lit 1) m) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe hm)
  have hq : Proof Γ (.le q (.mul q m)) :=
    .leRewrite (ax (.trans (.mulComm _ _) (mulOneLeft q))) (eqRefl _)
      (leMulLeft q hOne)
  exact leThenSucc (.leRewrite (eqRefl _) (.eqSymm he)
    (.leTrans hq (leRightAdd (.mul q m) r)))

def mulRightDistrib (q s m : Term) : EqProof
    (.mul (.add q s) m) (.add (.mul q m) (.mul s m)) :=
  .trans (.mulComm _ _) (.trans (.distrib _ _ _) (.add (.mulComm _ _) (.mulComm _ _)))

def shuffle (x y z : Term) : EqProof (.add (.add x y) z) (.add (.add x z) y) :=
  .trans (.addAssoc _ _ _) (.trans (.add (.refl _) (.addComm _ _)) (.symm (.addAssoc _ _ _)))

def liftEquality {Γ : List Formula} (a q m r cap s t : Term)
    (ha : Proof Γ (.eq a (.add (.mul q m) r)))
    (hcap : Proof Γ (.eq cap (.mul s m))) :
    Proof Γ (.eq (.add a (.mul cap t))
      (.add (.mul (.add q (.mul s t)) m) r)) := by
  have h₁ : Proof Γ
      (.eq (.add a (.mul cap t)) (.add (.add (.mul q m) r) (.mul (.mul s m) t))) :=
    .eqAdd ha (.eqMul hcap (eqRefl t))
  have ht : EqProof (.mul (.mul s m) t) (.mul (.mul s t) m) :=
    .trans (.mulAssoc _ _ _) (.trans (.mul (.refl _) (.mulComm _ _)) (.symm (.mulAssoc _ _ _)))
  exact .eqTrans h₁ (ax (.trans (.add (.refl _) ht)
    (.trans (shuffle (.mul q m) r (.mul (.mul s t) m))
      (.add (.symm (mulRightDistrib q (.mul s t) m)) (.refl _)))))

def liftContext : List Formula :=
  [.eq (.var 4) (.mul (.var 5) (.var 2)),
   .eq (.var 0) (.add (.mul (.var 1) (.var 2)) (.var 3)),
   .lt (.var 3) (.var 2), .lt (.lit 0) (.var 2)]
def newA : Term := .add (.var 0) (.mul (.var 4) (.var 6))
def liftedRemainder : Formula := .conj (.lt (.var 3) (.var 2))
  (.exB 12 (.succ newA)
    (.eq newA (.add (.mul (.var 12) (.var 2)) (.var 3))))

def liftOpen : Proof liftContext liftedRemainder := by
  have he : Proof liftContext
      (.eq newA (.add (.mul (.add (.var 1) (.mul (.var 5) (.var 6))) (.var 2)) (.var 3))) :=
    liftEquality (.var 0) (.var 1) (.var 2) (.var 3) (.var 4) (.var 5) (.var 6) (push hyp) hyp
  apply Proof.andI (push (push hyp))
  apply Proof.exBI 12 (.succ newA) (.add (.var 1) (.mul (.var 5) (.var 6))) (by decide)
    (quotientBound newA _ (.var 2) (.var 3) (push (push (push hyp))) he)
  exact he

def liftClosed : Proof []
    (.allN 0 (.allN 1 (.allN 2 (.allN 3 (.allN 4 (.allN 5 (.allN 6
      (.imp (.lt (.lit 0) (.var 2)) (.imp (.lt (.var 3) (.var 2))
       (.imp (.eq (.var 0) (.add (.mul (.var 1) (.var 2)) (.var 3)))
        (.imp (.eq (.var 4) (.mul (.var 5) (.var 2))) liftedRemainder))))))))))) :=
  .allI 0 rfl (.allI 1 rfl (.allI 2 rfl (.allI 3 rfl (.allI 4 rfl (.allI 5 rfl (.allI 6 rfl
    (.impI (.impI (.impI (.impI liftOpen))))))))))

example : liftedRemainder.bounded = true := by decide
example : liftedRemainder.safe 12 (.var 20) = true := by decide
#print axioms quotientBound
#print axioms liftEquality
#print axioms liftClosed
#eval ("modular_lift_certificate", profile liftClosed)
end MatematicaAbierta.Continuo.AritmeticaModularInternaRCA
