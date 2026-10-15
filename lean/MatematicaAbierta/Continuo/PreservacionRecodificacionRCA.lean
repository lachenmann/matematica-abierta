import MatematicaAbierta.Continuo.DatosRecodificacionBetaRCA

/-! M12/C11: explicit preservation and successor readings from the two
recoding selectors and the genuine fixed-b CRT readings. Trace(K+1) is not
part of the conclusion. No new inference rules or arithmetic axioms. -/
namespace MatematicaAbierta.Continuo.PreservacionRecodificacionRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA
open ContratoExtensionBetaRCA CRTCanalesSeparadosRCA DatosRecodificacionBetaRCA

def newA : Channel → Term | .u => .var 22 | .d => .var 25
def pointΓ (c : Channel) : List Formula :=
  [relation c (.var 16) (.var 17),readings c (newA c),spec c]
def pointProof (c : Channel) : Proof (pointΓ c)
    (beta (newA c) newB (.var 16) (.var 17)) := by
  have hr : Proof (pointΓ c) (relation c (.var 16) (.var 17)) := hyp
  have hs : Proof (pointΓ c) (spec c) := rca_ctx
  have hd : Proof (pointΓ c) (readings c (newA c)) := rca_ctx
  have hi := Proof.allBE 16 (.succ newK) (.var 16) (by cases c <;> decide) hd
    (leThenSucc (.andL hr))
  have hv := Proof.allBE 17 newT (.var 17) (by cases c <;> decide) hi (.andL (.andR hr))
  cases c
  · exact .impE hv (encode .u hs hr)
  · exact .impE hv (encode .d hs hr)
def pointClosed (c : Channel) : Proof []
    (.allN 16 (.allN 17 (.imp (spec c) (.imp (readings c (newA c))
      (.imp (relation c (.var 16) (.var 17)) (beta (newA c) newB (.var 16) (.var 17))))))) :=
  .allI 16 rfl (.allI 17 rfl (.impI (.impI (.impI (pointProof c)))))

def oldRelationClosed (c : Channel) : Proof []
    (.allN 16 (.allN 17 (.imp (.le (.var 16) stageBound)
      (.imp (.lt (.var 17) valueBound)
        (.imp (beta (codeA c) (codeB c) (.var 16) (.var 17))
          (relation c (.var 16) (.var 17))))))) := by
  apply Proof.allI 16 rfl
  apply Proof.allI 17 rfl
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  exact oldRelation c (.var 17) rca_ctx rca_ctx hyp

def preserveΓ (c : Channel) : List Formula := [readings c (newA c),spec c]
def preservation (c : Channel) : Proof (preserveΓ c)
    (preserves (codeA c) (codeB c) (newA c) newB) := by
  apply Proof.allBI 20 (.succ stageBound) (by cases c <;> decide) (by decide)
  apply Proof.allBI 21 valueBound (by cases c <;> decide) (by decide)
  apply Proof.impI
  let Γ : List Formula := [beta (codeA c) (codeB c) (.var 20) (.var 21),
    .lt (.var 21) valueBound,.lt (.var 20) (.succ stageBound)] ++ preserveΓ c
  have ho := Proof.allE 17 (.var 21) (by cases c <;> decide)
    (Proof.allE 16 (.var 20) (by cases c <;> decide) (oldRelationClosed c))
  have hk : Proof Γ (.le (.var 20) stageBound) :=
    belowSuccessor _ _ (rca_ctx : Proof Γ (.lt (.var 20) (.succ stageBound)))
  have hv : Proof Γ (.lt (.var 21) valueBound) := rca_ctx
  have hb : Proof Γ (beta (codeA c) (codeB c) (.var 20) (.var 21)) := hyp
  have hr : Proof Γ (relation c (.var 20) (.var 21)) := by
    cases c <;> exact Proof.impE (Proof.impE (Proof.impE (closed ho) hk) hv) hb
  have hp := Proof.allE 17 (.var 21) (by cases c <;> decide)
    (Proof.allE 16 (.var 20) (by cases c <;> decide) (pointClosed c))
  have hs : Proof Γ (spec c) := rca_ctx
  have hd : Proof Γ (readings c (newA c)) := rca_ctx
  cases c <;> exact Proof.impE (Proof.impE (Proof.impE (closed hp) hs) hd) hr

def lastΓ (c : Channel) : List Formula := [extensionInput,readings c (newA c),spec c]
def lastReading (c : Channel) : Proof (lastΓ c)
    (beta (newA c) newB newK (successorValue c)) := by
  have hp := Proof.allE 17 (successorValue c) (by cases c <;> decide)
    (Proof.allE 16 newK (by cases c <;> decide) (pointClosed c))
  have he : Proof (lastΓ c) extensionInput := hyp
  have hs : Proof (lastΓ c) (spec c) := rca_ctx
  have hd : Proof (lastΓ c) (readings c (newA c)) := rca_ctx
  cases c
  · exact Proof.impE (Proof.impE (Proof.impE (closed hp) hs) hd) (lastRelation .u he)
  · exact Proof.impE (Proof.impE (Proof.impE (closed hp) hs) hd) (lastRelation .d he)

def recodingBody : Formula :=
  .conj (preserves (.var 8) (.var 9) (.var 22) newB)
    (.conj (preserves (.var 10) (.var 11) (.var 25) newB)
      (.conj (beta (.var 22) newB newK (nextU (.var 1) (.var 7)))
        (beta (.var 25) newB newK (nextD (.var 2)))))
def combineΓ : List Formula :=
  [.conj (readings .u (.var 22)) (readings .d (.var 25)),spec .d,spec .u,extensionInput]
def recodingFromReadings : Proof combineΓ recodingBody := by
  have hu : Proof combineΓ (readings .u (.var 22)) := .andL hyp
  have hd : Proof combineΓ (readings .d (.var 25)) := .andR hyp
  have su : Proof combineΓ (spec .u) := rca_ctx
  have sd : Proof combineΓ (spec .d) := rca_ctx
  have he : Proof combineΓ extensionInput := rca_ctx
  have pu := Proof.impE (Proof.impE (closed (Proof.impI (Proof.impI (preservation .u)))) su) hu
  have pd := Proof.impE (Proof.impE (closed (Proof.impI (Proof.impI (preservation .d)))) sd) hd
  have lu := Proof.impE (Proof.impE (Proof.impE (closed (Proof.impI (Proof.impI (Proof.impI (lastReading .u))))) su) hu) he
  have ld := Proof.impE (Proof.impE (Proof.impE (closed (Proof.impI (Proof.impI (Proof.impI (lastReading .d))))) sd) hd) he
  exact .andI pu (.andI pd (.andI lu ld))

example : recodingBody.bounded = true := by decide
example : recodingBody.setFree = [] := by decide
example : recodingBody.numFree.contains 51 = false := by decide
example : (spec .u).safe 100 (pair (.var 20) (.var 21)) = true := by decide
#print axioms pointClosed
#print axioms oldRelationClosed
#print axioms preservation
#print axioms lastReading
#print axioms recodingFromReadings
#eval ("beta_recoding_preservation_and_successors", profile recodingFromReadings)
end MatematicaAbierta.Continuo.PreservacionRecodificacionRCA
