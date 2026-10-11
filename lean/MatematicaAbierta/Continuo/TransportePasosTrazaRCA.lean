import MatematicaAbierta.Continuo.RecodificacionNumericaBetaRCA

/-! M13/C12: transport the exact old step witnesses and base readings.
No new Proof constructors, existence hypotheses, comprehension or CRT. -/
namespace MatematicaAbierta.Continuo.TransportePasosTrazaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA
open ContratoExtensionBetaRCA CRTCanalesSeparadosRCA

def newNumeric (p : Formula) : Formula :=
  ((((p.subst 4 newT).subst 8 (.var 22)).subst 9 newB).subst 10 (.var 25)).subst 11 newB
def newStep (k : Term) : Formula := newNumeric (finiteTraceStep k)
def preserveU : Formula := preserves (.var 8) (.var 9) (.var 22) newB
def preserveD : Formula := preserves (.var 10) (.var 11) (.var 25) newB
def oldA : Channel → Term | .u => .var 8 | .d => .var 10
def oldB : Channel → Term | .u => .var 9 | .d => .var 11
def newA : Channel → Term | .u => .var 22 | .d => .var 25
def preserve : Channel → Formula | .u => preserveU | .d => preserveD

def pointΓ (c : Channel) : List Formula :=
  [beta (oldA c) (oldB c) (.var 16) (.var 17),.lt (.var 17) valueBound,
    .le (.var 16) stageBound,preserve c]
def point (c : Channel) : Proof (pointΓ c)
    (beta (newA c) newB (.var 16) (.var 17)) := by
  have hp : Proof (pointΓ c) (preserve c) := rca_ctx
  have hi : Proof (pointΓ c) (.le (.var 16) stageBound) := rca_ctx
  have hv : Proof (pointΓ c) (.lt (.var 17) valueBound) := rca_ctx
  cases c <;>
    exact .impE (.allBE 21 valueBound (.var 17) (by decide)
      (.allBE 20 (.succ stageBound) (.var 16) (by decide) hp (leThenSucc hi)) hv) hyp
def pointClosed (c : Channel) : Proof []
    (.allN 16 (.allN 17 (.imp (preserve c) (.imp (.le (.var 16) stageBound)
      (.imp (.lt (.var 17) valueBound)
        (.imp (beta (oldA c) (oldB c) (.var 16) (.var 17))
          (beta (newA c) newB (.var 16) (.var 17)))))))) :=
  .allI 16 rfl (.allI 17 rfl (.impI (.impI (.impI (.impI (point c))))))

def oldΓ : List Formula := [.lt (.var 0) stageBound,preserveD,preserveU,finiteTraceMatrix]
def oldLeaf : Formula := .conj (recurrenceValues (.var 0)) (traceValueRelations (.var 0))
def leafPrefix : List Formula :=
  [oldLeaf,.lt (.var 2) valueBound,
   .exB 2 valueBound oldLeaf,.lt (.var 1) valueBound,
   .exB 1 valueBound (.exB 2 valueBound oldLeaf),.lt (.var 7) (.lit 2),
   .exB 7 (.lit 2) (.exB 1 valueBound (.exB 2 valueBound oldLeaf)),.lt (.var 6) valueBound,
   .exB 6 valueBound (.exB 7 (.lit 2) (.exB 1 valueBound (.exB 2 valueBound oldLeaf))),
   .lt (.var 5) valueBound]
def leafΓ : List Formula := leafPrefix ++ oldΓ

def leaf : Proof leafΓ (newStep (.var 0)) := by
  have hw : Proof leafΓ oldLeaf := hyp
  have hk : Proof leafΓ (.lt (.var 0) stageBound) := rca_ctx
  have hu : Proof leafΓ preserveU := rca_ctx
  have hd : Proof leafΓ preserveD := rca_ctx
  have h5 : Proof leafΓ (.lt (.var 5) valueBound) := rca_ctx
  have h6 : Proof leafΓ (.lt (.var 6) valueBound) := rca_ctx
  have h1 : Proof leafΓ (.lt (.var 1) valueBound) := rca_ctx
  have h2 : Proof leafΓ (.lt (.var 2) valueBound) := rca_ctx
  have h7 : Proof leafΓ (.lt (.var 7) (.lit 2)) := rca_ctx
  have pu0 := Proof.allE 17 (.var 5) (by decide)
    (Proof.allE 16 (.var 0) (by decide) (pointClosed .u))
  have pd0 := Proof.allE 17 (.var 6) (by decide)
    (Proof.allE 16 (.var 0) (by decide) (pointClosed .d))
  have pu1 := Proof.allE 17 (.var 1) (by decide)
    (Proof.allE 16 (.succ (.var 0)) (by decide) (pointClosed .u))
  have pd1 := Proof.allE 17 (.var 2) (by decide)
    (Proof.allE 16 (.succ (.var 0)) (by decide) (pointClosed .d))
  have r5 := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed pu0) hu) (.ltLe hk)) h5) (.andL (.andR hw))
  have r6 := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed pd0) hd) (.ltLe hk)) h6) (.andL (.andR (.andR hw)))
  have r1 := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed pu1) hu) (.ltSuccLe hk)) h1) (.andL (.andR (.andR (.andR hw))))
  have r2 := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed pd1) hd) (.ltSuccLe hk)) h2) (.andR (.andR (.andR (.andR hw))))
  apply Proof.exBI 5 newT (.var 5) (by decide) (.ltTrans h5 (oldBoundBelow _))
  apply Proof.exBI 6 newT (.var 6) (by decide) (.ltTrans h6 (oldBoundBelow _))
  apply Proof.exBI 7 (.lit 2) (.var 7) (by decide) h7
  apply Proof.exBI 1 newT (.var 1) (by decide) (.ltTrans h1 (oldBoundBelow _))
  apply Proof.exBI 2 newT (.var 2) (by decide) (.ltTrans h2 (oldBoundBelow _))
  exact .andI (.andL hw) (.andI r5 (.andI r6 (.andI r1 r2)))

def oldStep : Proof oldΓ (newStep (.var 0)) := by
  have ht : Proof oldΓ finiteTraceMatrix := rca_ctx
  have hs : Proof oldΓ (finiteTraceStep (.var 0)) :=
    .allBE 0 stageBound (.var 0) (by decide) (.andR (.andR (.andR ht))) hyp
  apply Proof.exBE 5 valueBound (by decide) (by decide) (by decide) hs
  apply Proof.exBE 6 valueBound (by decide) (by decide) (by decide) hyp
  apply Proof.exBE 7 (.lit 2) (by decide) (by decide) (by decide) hyp
  apply Proof.exBE 1 valueBound (by decide) (by decide) (by decide) hyp
  apply Proof.exBE 2 valueBound (by decide) (by decide) (by decide) hyp
  exact leaf
def oldStepClosed : Proof [] (.imp finiteTraceMatrix (.imp preserveU (.imp preserveD
    (.allB 0 stageBound (newStep (.var 0)))))) := by
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  apply Proof.allBI 0 stageBound (by decide) (by decide)
  exact oldStep

example : (newStep (.var 0)).bounded = true := by decide
example : freshNum 5 oldΓ = true := by decide
example : freshNum 6 oldΓ = true := by decide
example : freshNum 7 oldΓ = true := by decide
example : freshNum 1 oldΓ = true := by decide
example : freshNum 2 oldΓ = true := by decide
example : (newStep (.var 0)).numFree.contains 5 = false := by decide
example : (newStep (.var 0)).numFree.contains 7 = false := by decide
#print axioms pointClosed
#print axioms leaf
#print axioms oldStepClosed
#eval ("old_steps_transported_exact_witnesses", profile oldStepClosed)
end MatematicaAbierta.Continuo.TransportePasosTrazaRCA
