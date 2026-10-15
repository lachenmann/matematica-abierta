import MatematicaAbierta.Continuo.CalculoConjuntosRCA
import MatematicaAbierta.Continuo.PreservacionRecodificacionRCA

/-! M12/C11: numerical beta recoding with one newly constructed parameter.
The only mathematical antecedent is the exact M07 extensionInput (existing
Trace(K), bounded terminal readings and the explicit admissible bit H04-03).
Sets are obtained by Delta1 comprehension, the common parameter by M09,
and codes by two renamed effective M11 CRT proof trees. No Trace(K+1) or
numericExtensionContract proof is asserted. Canonical RCA0 adequacy is C14. -/
namespace MatematicaAbierta.Continuo.RecodificacionNumericaBetaRCA
open CalculoRCA TrazasInduccionRCA ContratoExtensionBetaRCA
open CRTCanalesSeparadosRCA DatosRecodificacionBetaRCA PreservacionRecodificacionRCA
abbrev EProof := CalculoExistencialRCA.Proof
abbrev SProof := CalculoConjuntosRCA.Proof

def large : Formula := ParametroUniformeBetaRCA.largeMatrix newK newT newB
def codeResult : Formula := .exN 22 (.exN 25 recodingBody)
def recodingExists : Formula := .exN 40 (.conj (.lt newT newB) (.conj cm codeResult))
def recodingGoal : Formula := .imp extensionInput recodingExists
def Γsets : List Formula := [spec .d,spec .u,large,extensionInput]
def Γextract : List Formula :=
  [.conj (readings .u (.var 22)) (readings .d (.var 25)),
    .exN 25 (.conj (readings .u (.var 22)) (readings .d (.var 25)))] ++ Γsets

def dataU : CalculoOrdenRCA.Proof Γsets (data .u) := by
  have h := CalculoOrdenRCA.Proof.impI (CalculoOrdenRCA.Proof.impI
    (CalculoOrdenRCA.Proof.impI (residueDataFromTrace .u)))
  have he : CalculoOrdenRCA.Proof Γsets extensionInput := rca_ctx
  have hl : CalculoOrdenRCA.Proof Γsets large := rca_ctx
  have hs : CalculoOrdenRCA.Proof Γsets (spec .u) := rca_ctx
  exact .impE (.impE (.impE (SelectoresInternosRCA.closed h) he) (.andL hl)) hs

def dataD : CalculoOrdenRCA.Proof Γsets (data .d) := by
  have h := CalculoOrdenRCA.Proof.impI (CalculoOrdenRCA.Proof.impI
    (CalculoOrdenRCA.Proof.impI (residueDataFromTrace .d)))
  have he : CalculoOrdenRCA.Proof Γsets extensionInput := rca_ctx
  have hl : CalculoOrdenRCA.Proof Γsets large := rca_ctx
  have hs : CalculoOrdenRCA.Proof Γsets (spec .d) := rca_ctx
  exact .impE (.impE (.impE (SelectoresInternosRCA.closed h) he) (.andL hl)) hs

def atTwoCodes : EProof Γsets bothCodes := by
  have hl : CalculoOrdenRCA.Proof Γsets large := rca_ctx
  exact .impE (.impE (.impE (CalculoExistencialRCA.closed twoCodesClosed)
    (.embed (.andR hl))) (.embed dataU)) (.embed dataD)

def extraction : CalculoOrdenRCA.Proof Γextract recodingBody :=
  .weaken (by
    intro f hf
    change f ∈ [Formula.conj (readings .u (.var 22)) (readings .d (.var 25)),
      spec .d,spec .u,extensionInput] at hf
    cases hf with
    | head => exact List.mem_cons_self
    | tail _ hf =>
      cases hf with
      | head => repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem
      | tail _ hf =>
        cases hf with
        | head => repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem
        | tail _ hf =>
          cases hf with
          | head => repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem
          | tail _ hf => cases hf) recodingFromReadings

def codesRecoded : EProof Γsets codeResult := by
  apply CalculoExistencialRCA.Proof.exNE 22 (by decide) (by decide) atTwoCodes
  apply CalculoExistencialRCA.Proof.exNE 25 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNI 22 (.var 22) (by decide)
  apply CalculoExistencialRCA.Proof.exNI 25 (.var 25) (by decide)
  exact .embed extraction

def commonParameter : EProof [] (.exN 40 large) :=
  .allE 4 newT (by decide) (.allE 3 newK (by decide) ParametroUniformeBetaRCA.uniformParameter)

def recoding : SProof [] recodingGoal := by
  apply CalculoConjuntosRCA.Proof.impI
  apply CalculoConjuntosRCA.Proof.exNE 40 (by decide) (by decide)
    (CalculoConjuntosRCA.closed (.embed commonParameter))
  apply CalculoConjuntosRCA.Proof.exSE 3 (by decide) (by decide)
    (CalculoConjuntosRCA.closed (CalculoConjuntosRCA.old (finiteDataExists .u)))
  apply CalculoConjuntosRCA.Proof.exSE 4 (by decide) (by decide)
    (CalculoConjuntosRCA.closed (CalculoConjuntosRCA.old (finiteDataExists .d)))
  apply CalculoConjuntosRCA.Proof.exNI 40 newB (by decide)
  have hl : SProof Γsets large :=
    .hypothesis (List.mem_cons_of_mem _ (List.mem_cons_of_mem _ List.mem_cons_self))
  exact .andI (.andL hl) (.andI (.andR hl) (.embed codesRecoded))

def universalRecodingGoal : Formula :=
  [3,4,8,9,10,11,1,2,7].foldr Formula.allN recodingGoal
def universalRecoding : SProof [] universalRecodingGoal :=
  .allI 3 rfl (.allI 4 rfl (.allI 8 rfl (.allI 9 rfl (.allI 10 rfl
    (.allI 11 rfl (.allI 1 rfl (.allI 2 rfl (.allI 7 rfl recoding))))))))

example : universalRecodingGoal.numFree = [] := by decide
example : universalRecodingGoal.setFree.all (· == 2) = true := by decide
#print axioms universalRecoding

-- Exact syntax and rejection controls: neither data set can escape elimination;
-- B remains set 2. No endpoint trace or global adequacy conclusion is present.
example : recodingGoal.setFree.all (· == 2) = true := by decide
example : recodingGoal.setFree.contains 2 = true := by decide
example : recodingGoal.setFree.contains 3 = false := by decide
example : recodingGoal.setFree.contains 4 = false := by decide
example : freshSet 3 [large,extensionInput] = true := by decide
example : freshSet 4 [spec .u,large,extensionInput] = true := by decide
example : recodingExists.setFree = [] := by decide
example : freshNum 40 [extensionInput] = true := by decide
example : freshNum 22 Γsets = true := by decide
example : freshNum 25 [Formula.exN 25 (.conj (readings .u (.var 22)) (readings .d (.var 25))),spec .d,spec .u,large,extensionInput] = true := by decide
example : recodingExists.numFree.contains 40 = false := by decide
example : (spec .u).setFree.contains 4 = false := by decide
example : (spec .d).setFree.contains 3 = false := by decide
example : codeResult.bounded = false := by decide
example : recodingBody.bounded = true := by decide
#print axioms dataU
#print axioms dataD
#print axioms codesRecoded
#print axioms commonParameter
#print axioms recoding
#eval ("common_parameter_above_new_bound", CalculoExistencialRCA.profile commonParameter)
#eval ("two_finite_residue_contracts_U", CalculoOrdenRCA.profile dataU)
#eval ("two_finite_residue_contracts_D", CalculoOrdenRCA.profile dataD)
#eval ("codes_with_preservation_and_successors", CalculoExistencialRCA.profile codesRecoded)
#eval ("C11_numeric_beta_recoding", CalculoConjuntosRCA.profile recoding)
end MatematicaAbierta.Continuo.RecodificacionNumericaBetaRCA
