import MatematicaAbierta.Continuo.RenombradoConjuntosRCA
import MatematicaAbierta.Continuo.ContratoExtensionBetaRCA

/-! M12: two genuine fixed-b CRT proof trees with distinct finite data sets.
Only CM and the two explicit residue-data contracts are antecedents here.
No existence of these data sets, Trace extension or recoding is presumed. -/
namespace MatematicaAbierta.Continuo.CRTCanalesSeparadosRCA
open CalculoRCA SelectoresInternosRCA ContratoExtensionBetaRCA
open RenombradoConjuntosRCA
abbrev EProof := CalculoExistencialRCA.Proof

def dataSet : Channel → ℕ | .u => 3 | .d => 4
def setMap (c : Channel) : ℕ → ℕ := swap 2 (dataSet c)
def newK : Term := .succ (.var 3)
def newT : Term := boundCandidate (.var 4)
def newB : Term := .var 40

def instantiate (p : Formula) : Formula :=
  ((p.subst 0 newK).subst 4 newT).subst 9 newB

def data (c : Channel) : Formula :=
  instantiate (rename (setMap c) InvarianteCRTParcialRCA.residueData)
def readings (c : Channel) (a : Term) : Formula :=
  .allB 16 (.succ newK) (.allB 17 newT
    (.imp (.member (TrazasInduccionRCA.pair (.var 16) (.var 17)) (dataSet c))
      (TrazasInduccionRCA.beta a newB (.var 16) (.var 17))))
def cm : Formula := MultiploComunUniformeRCA.cm newK newB
def codeExists (c : Channel) (x : ℕ) : Formula := .exN x (readings c (.var x))
def Γdata : List Formula := [data .d,data .u,cm]

def atCRT (c : Channel) : EProof Γdata (codeExists c 51) := by
  have h := logical (setMap c) (swap_injective 2 (dataSet c)) CRTFinitoUniformeRCA.fixedBCRT
  have hn := CalculoExistencialRCA.Proof.allE 0 newK (by cases c <;> decide) h
  have ht := CalculoExistencialRCA.Proof.allE 4 newT (by cases c <;> decide) hn
  have hb := CalculoExistencialRCA.Proof.allE 9 newB (by cases c <;> decide) ht
  have hc : EProof Γdata cm := .hypothesis (List.mem_cons_of_mem _ (List.mem_cons_of_mem _ List.mem_cons_self))
  have hd : EProof Γdata (data c) := by
    cases c
    · exact .hypothesis (List.mem_cons_of_mem _ List.mem_cons_self)
    · exact CalculoExistencialRCA.hyp
  cases c <;> exact .impE (.impE (CalculoExistencialRCA.closed hb) hc) hd

def codeNameU : EProof Γdata (codeExists .u 22) := by
  apply CalculoExistencialRCA.Proof.exNE 51 (by decide) (by decide) (atCRT .u)
  apply CalculoExistencialRCA.Proof.exNI 22 (.var 51) (by decide)
  exact CalculoExistencialRCA.hyp
def codeNameD : EProof Γdata (codeExists .d 25) := by
  apply CalculoExistencialRCA.Proof.exNE 51 (by decide) (by decide) (atCRT .d)
  apply CalculoExistencialRCA.Proof.exNI 25 (.var 51) (by decide)
  exact CalculoExistencialRCA.hyp

def bothCodes : Formula := .exN 22 (.exN 25
  (.conj (readings .u (.var 22)) (readings .d (.var 25))))
def twoCodes : EProof Γdata bothCodes := by
  apply CalculoExistencialRCA.Proof.exNE 22 (by decide) (by decide) codeNameU
  apply CalculoExistencialRCA.Proof.exNE 25 (by decide) (by decide) (CalculoExistencialRCA.push codeNameD)
  apply CalculoExistencialRCA.Proof.exNI 22 (.var 22) (by decide)
  apply CalculoExistencialRCA.Proof.exNI 25 (.var 25) (by decide)
  exact .andI (CalculoExistencialRCA.push CalculoExistencialRCA.hyp) CalculoExistencialRCA.hyp

def twoCodesGoal : Formula := .imp cm (.imp (data .u) (.imp (data .d) bothCodes))
def twoCodesClosed : EProof [] twoCodesGoal := .impI (.impI (.impI twoCodes))

-- The reserved bit graph remains a separate antecedent, never renamed.
def withBits : EProof [admissibleBit] twoCodesGoal :=
  CalculoExistencialRCA.closed twoCodesClosed
example : admissibleBit.setFree = [2] := rfl
example : (data .u).setFree.all (· == 3) = true := by decide
example : (data .d).setFree.all (· == 4) = true := by decide
example : bothCodes.setFree.contains 2 = false := by decide
example : freshNum 22 Γdata = true := by decide
example : freshNum 25 [readings .u (.var 22)] = true := by decide
example : bothCodes.numFree.contains 51 = false := by decide
example : (readings .u (.var 22)).safe 22 (.var 51) = true := by decide
example : (readings .d (.var 25)).safe 25 (.var 51) = true := by decide
#print axioms atCRT
#print axioms codeNameU
#print axioms codeNameD
#print axioms twoCodesClosed
#print axioms withBits
#eval ("two_distinct_sets_same_beta_parameter", CalculoExistencialRCA.profile twoCodesClosed)
end MatematicaAbierta.Continuo.CRTCanalesSeparadosRCA
