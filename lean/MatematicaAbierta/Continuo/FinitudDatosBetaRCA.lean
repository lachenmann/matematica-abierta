import MatematicaAbierta.Continuo.DatosRecodificacionBetaRCA

/-! M12: a numerical bound for the entire finite set, not only its values.
Every coded pair lies below P(K+1,T')+1 by internal polynomial monotonicity.
No ambient finiteness theorem or code-existence axiom is used. -/
namespace MatematicaAbierta.Continuo.FinitudDatosBetaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA EmparejamientoInternoRCA
open SelectoresInternosRCA CRTCanalesSeparadosRCA DatosRecodificacionBetaRCA

def finiteBound : Term := .succ (pair newK newT)
def Γ (c : Channel) : List Formula := [.member (.var 100) (dataSet c),spec c]
def leafΓ (c : Channel) : List Formula :=
  [body c,.lt (.var 102) (.succ (.var 100)),
    .exB 102 (.succ (.var 100)) (body c),.lt (.var 101) (.succ (.var 100))] ++ Γ c

def leaf (c : Channel) : Proof (leafΓ c) (.lt (.var 100) finiteBound) := by
  have hw : Proof (leafΓ c) (body c) := hyp
  have hr : Proof (leafΓ c) (relation c (.var 101) (.var 102)) := .andR hw
  have hk := Proof.andL hr
  have hv := Proof.ltLe (Proof.andL (Proof.andR hr))
  have hp : Proof (leafΓ c) (.le (pair (.var 101) (.var 102)) (pair newK newT)) :=
    .leAdd (squareMonotone (.leAdd hk hv)) hk
  exact leThenSucc (.leRewrite (.eqSymm (.andL hw)) (eqRefl _) hp)

def finite (c : Channel) : Proof [spec c]
    (.allN 100 (.imp (.member (.var 100) (dataSet c)) (.lt (.var 100) finiteBound))) := by
  apply Proof.allI 100 (by cases c <;> decide)
  apply Proof.impI
  have hs := Proof.allE 100 (.var 100) (by cases c <;> decide) (push hyp : Proof (Γ c) (spec c))
  have hm : Proof (Γ c) (matrix c) := by
    cases c <;> exact Proof.impE (.andL hs) hyp
  apply Proof.exBE 101 (.succ (.var 100)) (by cases c <;> decide) (by decide) (by decide) hm
  apply Proof.exBE 102 (.succ (.var 100)) (by cases c <;> decide) (by decide) (by decide) hyp
  exact leaf c

example : finiteBound.vars.contains 101 = false := by decide
example : finiteBound.vars.contains 102 = false := by decide
example : (Formula.lt (.var 100) finiteBound).bounded = true := by decide
#print axioms leaf
#print axioms finite
#eval ("DU_finite_set_polynomial_bound", profile (Proof.impI (finite .u)))
#eval ("DD_finite_set_polynomial_bound", profile (Proof.impI (finite .d)))
end MatematicaAbierta.Continuo.FinitudDatosBetaRCA
