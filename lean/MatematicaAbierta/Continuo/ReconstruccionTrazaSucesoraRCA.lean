import MatematicaAbierta.Continuo.TransportePasosTrazaRCA

/-! M13/C12: the new last step, transported bases, and all exact fields of
finiteTraceMatrix at K+1. H04-03 is kept in extensionInput, not discharged. -/
namespace MatematicaAbierta.Continuo.ReconstruccionTrazaSucesoraRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA
open ContratoExtensionBetaRCA CRTCanalesSeparadosRCA TransportePasosTrazaRCA
open PreservacionRecodificacionRCA
open DatosRecodificacionBetaRCA

def terminalU : Term := .var 131
def terminalD : Term := .var 132
def terminalBit : Term := .var 137
def terminalInput : Formula :=
  .conj (.lt terminalU valueBound) (.conj (.lt terminalD valueBound)
    (.conj (beta (.var 22) newB stageBound terminalU)
      (.conj (beta (.var 25) newB stageBound terminalD)
        (.conj (beta (.var 22) newB newK (nextU terminalU terminalBit))
          (.conj (beta (.var 25) newB newK (nextD terminalD))
            (.conj (gb stageBound terminalBit) (.le terminalBit (.lit 1))))))))
def terminalStep : Proof [terminalInput] (newStep stageBound) := by
  have h : Proof [terminalInput] terminalInput := hyp
  have hu := Proof.andL h
  have hd := Proof.andL (.andR h)
  have hb := Proof.andR (.andR (.andR (.andR (.andR (.andR (.andR h))))))
  have bitBound : Proof [terminalInput] (.lt terminalBit (.lit 2)) :=
    .leLtTrans hb (.ltRewrite (eqRefl _) (ax (.symm (.literalSucc 1))) (ltSucc (.lit 1)))
  apply Proof.exBI 5 newT terminalU (by decide) (.ltTrans hu (oldBoundBelow _))
  apply Proof.exBI 6 newT terminalD (by decide) (.ltTrans hd (oldBoundBelow _))
  apply Proof.exBI 7 (.lit 2) terminalBit (by decide) bitBound
  apply Proof.exBI 1 newT (nextU terminalU terminalBit) (by decide) (nextUBound _ _ _ hu hb)
  apply Proof.exBI 2 newT (nextD terminalD) (by decide) (nextDBound _ _ hd)
  exact .andI
    (.andI (.andL (.andR (.andR (.andR (.andR (.andR (.andR h)))))))
      (.andI (eqRefl _) (.andI (eqRefl _) hb)))
    (.andI (.andL (.andR (.andR h)))
      (.andI (.andL (.andR (.andR (.andR h))))
        (.andI (.andL (.andR (.andR (.andR (.andR h)))))
          (.andL (.andR (.andR (.andR (.andR (.andR h)))))))))
def terminalClosed : Proof [] (.allN 131 (.allN 132 (.allN 137
    (.imp terminalInput (newStep stageBound))))) :=
  .allI 131 rfl (.allI 132 rfl (.allI 137 rfl (.impI terminalStep)))

def newTrace : Formula := newNumeric (finiteTraceMatrix.subst 3 newK)
def traceΓ : List Formula := [recodingBody,extensionInput]

def aliasΓ : List Formula :=
  [.eq terminalBit (.var 7),.lt terminalBit (.lit 2),
   .eq terminalD (.var 2),.lt terminalD valueBound,
   .eq terminalU (.var 1),.lt terminalU valueBound] ++ traceΓ
def aliasStep : Proof aliasΓ (newStep stageBound) := by
  have he : Proof aliasΓ extensionInput := rca_ctx
  have hr : Proof aliasΓ recodingBody := rca_ctx
  have hu : Proof aliasΓ (.lt terminalU valueBound) := rca_ctx
  have hd : Proof aliasΓ (.lt terminalD valueBound) := rca_ctx
  have eu : Proof aliasΓ (.eq terminalU (.var 1)) := rca_ctx
  have ed : Proof aliasΓ (.eq terminalD (.var 2)) := rca_ctx
  have eb : Proof aliasΓ (.eq terminalBit (.var 7)) := hyp
  have pu := Proof.andL hr
  have pd := Proof.andL (.andR hr)
  have oldU := Proof.andL (.andR (.andR (.andR he)))
  have oldD := Proof.andL (.andR (.andR (.andR (.andR he))))
  have admissible := Proof.andR (.andR (.andR (.andR (.andR he))))
  have uPoint := Proof.allE 17 (.var 1) (by decide)
    (Proof.allE 16 stageBound (by decide) (TransportePasosTrazaRCA.pointClosed .u))
  have dPoint := Proof.allE 17 (.var 2) (by decide)
    (Proof.allE 16 stageBound (by decide) (TransportePasosTrazaRCA.pointClosed .d))
  have readU := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed uPoint) pu) (leRefl _)) (.andL (.andR he))) oldU
  have readD := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed dPoint) pd) (leRefl _)) (.andL (.andR (.andR he)))) oldD
  have ru : Proof aliasΓ (beta (.var 22) newB stageBound terminalU) :=
    .eqSubst (beta (.var 22) newB stageBound (.var 146)) 146 (.var 1) terminalU
      (by decide) (by decide) (.eqSymm eu) readU
  have rd : Proof aliasΓ (beta (.var 25) newB stageBound terminalD) :=
    .eqSubst (beta (.var 25) newB stageBound (.var 146)) 146 (.var 2) terminalD
      (by decide) (by decide) (.eqSymm ed) readD
  have esu : Proof aliasΓ (.eq (nextU terminalU terminalBit) (nextU (.var 1) (.var 7))) :=
    .eqAdd (.eqMul (eqRefl _) eu) (.eqMul (eqRefl _) eb)
  have esd : Proof aliasΓ (.eq (nextD terminalD) (nextD (.var 2))) :=
    .eqMul (eqRefl _) ed
  have su : Proof aliasΓ (beta (.var 22) newB newK (nextU terminalU terminalBit)) :=
    .eqSubst (beta (.var 22) newB newK (.var 146)) 146 (nextU (.var 1) (.var 7)) (nextU terminalU terminalBit)
      (by decide) (by decide) (.eqSymm esu) (.andL (.andR (.andR hr)))
  have sd : Proof aliasΓ (beta (.var 25) newB newK (nextD terminalD)) :=
    .eqSubst (beta (.var 25) newB newK (.var 146)) 146 (nextD (.var 2)) (nextD terminalD)
      (by decide) (by decide) (.eqSymm esd) (.andR (.andR (.andR hr)))
  have gbAlias : Proof aliasΓ (gb stageBound terminalBit) :=
    .eqSubst (gb stageBound (.var 146)) 146 (.var 7) terminalBit
      (by decide) (by decide) (.eqSymm eb) (.andL admissible)
  have hbAlias : Proof aliasΓ (.le terminalBit (.lit 1)) :=
    .leRewrite (.eqSymm eb) (eqRefl _) (.andR admissible)
  have hTerminal := Proof.allE 137 terminalBit (by decide)
    (Proof.allE 132 terminalD (by decide) (Proof.allE 131 terminalU (by decide) terminalClosed))
  exact .impE (closed hTerminal) (.andI hu (.andI hd (.andI ru (.andI rd
    (.andI su (.andI sd (.andI gbAlias hbAlias)))))))

def lastStep : Proof traceΓ (newStep stageBound) := by
  have he : Proof traceΓ extensionInput := rca_ctx
  have hU : Proof traceΓ (.exB 131 valueBound (.eq terminalU (.var 1))) :=
    .exBI 131 valueBound (.var 1) (by decide) (.andL (.andR he)) (eqRefl _)
  have hD : Proof traceΓ (.exB 132 valueBound (.eq terminalD (.var 2))) :=
    .exBI 132 valueBound (.var 2) (by decide) (.andL (.andR (.andR he))) (eqRefl _)
  have hb : Proof traceΓ (.le (.var 7) (.lit 1)) :=
    .andR (.andR (.andR (.andR (.andR (.andR he)))))
  have hBit : Proof traceΓ (.exB 137 (.lit 2) (.eq terminalBit (.var 7))) :=
    .exBI 137 (.lit 2) (.var 7) (by decide)
      (.leLtTrans hb (.ltRewrite (eqRefl _) (ax (.symm (.literalSucc 1))) (ltSucc (.lit 1)))) (eqRefl _)
  apply Proof.exBE 131 valueBound (by decide) (by decide) (by decide) hU
  apply Proof.exBE 132 valueBound (by decide) (by decide) (by decide) (push (push hD))
  apply Proof.exBE 137 (.lit 2) (by decide) (by decide) (by decide) (push (push (push (push hBit))))
  exact aliasStep

def previousSteps : Proof traceΓ (.allB 0 stageBound (newStep (.var 0))) := by
  have he : Proof traceΓ extensionInput := rca_ctx
  have hr : Proof traceΓ recodingBody := hyp
  exact .impE (.impE (.impE (closed oldStepClosed) (.andL he)) (.andL hr)) (.andL (.andR hr))

def rebuild : Proof traceΓ newTrace := by
  have he : Proof traceΓ extensionInput := rca_ctx
  have hr : Proof traceΓ recodingBody := hyp
  have ht := Proof.andL he
  have hT := Proof.andL ht
  have hu0 := Proof.andL (.andR ht)
  have hd0 := Proof.andL (.andR (.andR ht))
  have pu := Proof.andL hr
  have pd := Proof.andL (.andR hr)
  have uPoint := Proof.allE 17 (.lit 0) (by decide)
    (Proof.allE 16 (.lit 0) (by decide) (TransportePasosTrazaRCA.pointClosed .u))
  have dPoint := Proof.allE 17 (.lit 1) (by decide)
    (Proof.allE 16 (.lit 0) (by decide) (TransportePasosTrazaRCA.pointClosed .d))
  have zeroBelow : Proof traceΓ (.lt (.lit 0) valueBound) :=
    .ltTrans (.embed ConstruccionBaseTrazaRCA.zeroLtOne) hT
  have newU0 := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed uPoint) pu) (.zeroLe _)) zeroBelow) hu0
  have newD0 := Proof.impE (Proof.impE (Proof.impE (Proof.impE (closed dPoint) pd) (.zeroLe _)) hT) hd0
  apply Proof.andI (.ltTrans hT (oldBoundBelow _))
  apply Proof.andI newU0
  apply Proof.andI newD0
  apply Proof.allBI 0 newK (by decide) (by decide)
  let Γ := Formula.lt (.var 0) newK :: traceΓ
  have oldAll : Proof Γ (.allB 0 stageBound (newStep (.var 0))) := push previousSteps
  have last : Proof Γ (newStep stageBound) := push lastStep
  apply Proof.orderCases (.var 0) stageBound
  · exact .allBE 0 stageBound (.var 0) (by decide) (push oldAll) hyp
  · exact Proof.eqSubst (newStep (.var 145)) 145 stageBound (.var 0)
      (by decide) (by decide) (.eqSymm hyp) (push last)
  · have below : Proof (Formula.lt stageBound (.var 0) :: Γ) (.le (.var 0) stageBound) :=
      belowSuccessor _ _ (push hyp)
    exact .botE (.ltIrrefl (.ltLeTrans hyp below))

def rebuildClosed : Proof [] (.imp extensionInput (.imp recodingBody newTrace)) :=
  .impI (.impI rebuild)

example : newTrace = ((extendedTrace.subst 24 newT).subst 23 newB).subst 26 newB := by decide
example : newTrace.bounded = true := by decide
example : freshNum 0 traceΓ = true := by decide
example : (newStep (.var 145)).safe 145 stageBound = true := by decide
example : (newStep (.var 145)).safe 145 (.var 0) = true := by decide
example : (newStep stageBound).numFree.contains 131 = false := by decide
example : (newStep stageBound).numFree.contains 132 = false := by decide
example : (newStep stageBound).numFree.contains 137 = false := by decide
example : newTrace.setFree.all (· == 2) = true := by decide
example : (newStep stageBound).numFree.contains 5 = false := by decide
example : (Formula.exB 1 newT (.eq (.var 5) (.var 1))).safe 5 (.var 1) = false := by decide
#print axioms terminalClosed
#print axioms lastStep
#print axioms previousSteps
#print axioms rebuildClosed
#eval ("last_step_five_bounded_witnesses", profile terminalClosed)
#eval ("last_step_terminal_readings_from_C11", profile (Proof.impI (Proof.impI lastStep)))
#eval ("complete_successor_finite_trace", profile rebuildClosed)
end MatematicaAbierta.Continuo.ReconstruccionTrazaSucesoraRCA
