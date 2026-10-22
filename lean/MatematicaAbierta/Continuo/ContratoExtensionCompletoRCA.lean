import MatematicaAbierta.Continuo.ReconstruccionTrazaSucesoraRCA

/-! M13/C12: exact original numericExtensionContract, not a weakened goal.
Five original numerical existentials, b_U'=b_D'=b', ordinary guarded logic.
H04-03/C13 and canonical adequacy C14 remain explicitly separate. -/
namespace MatematicaAbierta.Continuo.ContratoExtensionCompletoRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA
open ContratoExtensionBetaRCA CRTCanalesSeparadosRCA PreservacionRecodificacionRCA
open ReconstruccionTrazaSucesoraRCA
abbrev SProof := CalculoConjuntosRCA.Proof

def assembled : SProof traceΓ extensionExists := by
  apply CalculoConjuntosRCA.Proof.exNI 24 newT (by decide)
  apply CalculoConjuntosRCA.Proof.exNI 22 (.var 22) (by decide)
  apply CalculoConjuntosRCA.Proof.exNI 23 newB (by decide)
  apply CalculoConjuntosRCA.Proof.exNI 25 (.var 25) (by decide)
  apply CalculoConjuntosRCA.Proof.exNI 26 newB (by decide)
  apply CalculoConjuntosRCA.old
  have hr : CalculoOrdenRCA.Proof traceΓ recodingBody := hyp
  exact .andI (oldBoundBelow _) (.andI (.andL hr) (.andI (.andL (.andR hr))
    (.andI (.andL (.andR (.andR hr))) (.andI (.andR (.andR (.andR hr))) rebuild))))

def assembledClosed : SProof [] (.imp extensionInput (.imp recodingBody extensionExists)) :=
  .impI (.impI assembled)

def C11 : SProof [] RecodificacionNumericaBetaRCA.recodingGoal := by
  have h0 := CalculoConjuntosRCA.Proof.allE 3 (.var 3) (by decide) RecodificacionNumericaBetaRCA.universalRecoding
  have h1 := CalculoConjuntosRCA.Proof.allE 4 (.var 4) (by decide) h0
  have h2 := CalculoConjuntosRCA.Proof.allE 8 (.var 8) (by decide) h1
  have h3 := CalculoConjuntosRCA.Proof.allE 9 (.var 9) (by decide) h2
  have h4 := CalculoConjuntosRCA.Proof.allE 10 (.var 10) (by decide) h3
  have h5 := CalculoConjuntosRCA.Proof.allE 11 (.var 11) (by decide) h4
  have h6 := CalculoConjuntosRCA.Proof.allE 1 (.var 1) (by decide) h5
  have h7 := CalculoConjuntosRCA.Proof.allE 2 (.var 2) (by decide) h6
  exact CalculoConjuntosRCA.Proof.allE 7 (.var 7) (by decide) h7

def result : SProof [] (.imp extensionInput extensionExists) := by
  apply CalculoConjuntosRCA.Proof.impI
  have recoded : SProof [extensionInput] RecodificacionNumericaBetaRCA.recodingExists :=
    .impE (CalculoConjuntosRCA.closed C11) CalculoConjuntosRCA.hyp
  apply CalculoConjuntosRCA.Proof.exNE 40 (by decide) (by decide) recoded
  have codes : SProof [Formula.conj (Formula.lt newT newB)
      (Formula.conj cm RecodificacionNumericaBetaRCA.codeResult),extensionInput]
      RecodificacionNumericaBetaRCA.codeResult :=
    .andR (.andR CalculoConjuntosRCA.hyp)
  apply CalculoConjuntosRCA.Proof.exNE 22 (by decide) (by decide) codes
  apply CalculoConjuntosRCA.Proof.exNE 25 (by decide) (by decide) CalculoConjuntosRCA.hyp
  have he : SProof [recodingBody,Formula.exN 25 recodingBody,
      Formula.conj (Formula.lt newT newB) (Formula.conj cm RecodificacionNumericaBetaRCA.codeResult),extensionInput]
      extensionInput := .hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)
  exact .impE (.impE (CalculoConjuntosRCA.closed assembledClosed) he) CalculoConjuntosRCA.hyp

def numericExtension : SProof [] numericExtensionContract :=
  .allI 3 rfl (.allI 4 rfl (.allI 8 rfl (.allI 9 rfl (.allI 10 rfl
    (.allI 11 rfl (.allI 1 rfl (.allI 2 rfl (.allI 7 rfl result))))))))

example : numericExtensionContract.numFree = [] := by decide
example : numericExtensionContract.setFree = [2,2,2] := by decide
example : extensionExists.numFree.contains 40 = false := by decide
example : extensionExists.numFree.contains 22 = false := by decide
example : extensionExists.numFree.contains 25 = false := by decide
example : freshNum 40 [extensionInput] = true := by decide
example : freshNum 22 [Formula.conj (Formula.lt newT newB)
    (Formula.conj cm RecodificacionNumericaBetaRCA.codeResult),extensionInput] = true := by decide
example : extensionExists.setFree.all (· == 2) = true := by decide
example : extensionBody.safe 26 newB = true := by decide
example : extendedTrace.safe 24 newT = true := by decide
#print axioms assembledClosed
#print axioms C11
#print axioms result
#print axioms numericExtension
#eval ("five_original_numeric_existentials", CalculoConjuntosRCA.profile assembledClosed)
#eval ("C12_exact_numericExtensionContract", CalculoConjuntosRCA.profile numericExtension)
end MatematicaAbierta.Continuo.ContratoExtensionCompletoRCA
