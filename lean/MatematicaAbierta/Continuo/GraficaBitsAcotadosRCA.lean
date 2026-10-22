import MatematicaAbierta.Continuo.ContratoExtensionCompletoRCA

/-! M14/C13: bounded finite-image search, using graph set 5, bits set 2.
No total function is extracted from the input relation. No infinite range.
All set existence below is an actual M05 Delta1-comprehension tree. -/
namespace MatematicaAbierta.Continuo.GraficaBitsAcotadosRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA
open EmparejamientoInternoRCA

def hit (j : Term) : Formula := .exB 155 (.var 156) (.member (pair (.var 155) j) 5)
def neg (p : Formula) : Formula := .imp p .bot
def criterion (j e : Term) : Formula := .conj (.lt e (.lit 2)) (iffF (.eq e (.lit 1)) (hit j))
def matrix (z : Term) : Formula :=
  .exB 153 (.succ z) (.exB 154 (.succ z)
    (.conj (.eq z (pair (.var 153) (.var 154))) (criterion (.var 153) (.var 154))))
def spec : Formula := .allN 152 (iffF (.member (.var 152) 2) (matrix (.var 152)))
def graphExists : Formula := .exS 2 spec

-- These are explicit input contracts, never axioms or Lean total functions.
def totalSingleGraph : Formula := .conj
  (.allN 158 (.exN 159 (.member (pair (.var 158) (.var 159)) 5)))
  (.allN 158 (.allN 159 (.allN 160
    (.imp (.conj (.member (pair (.var 158) (.var 159)) 5)
      (.member (pair (.var 158) (.var 160)) 5)) (.eq (.var 159) (.var 160))))))
def injectiveGraph : Formula := .allN 158 (.allN 159 (.allN 160
  (.imp (.conj (.member (pair (.var 158) (.var 160)) 5)
    (.member (pair (.var 159) (.var 160)) 5)) (.eq (.var 158) (.var 159)))))
def H0401 : Formula := .conj totalSingleGraph injectiveGraph
-- Finite cutoff contract retained as a premise; no proof of its existence.
def H0402 : Formula := .exN 163 (.allB 158 (.var 156) (.allN 159
  (.imp (.member (pair (.var 158) (.var 159)) 5) (.lt (.var 159) (.var 163)))))
def antecedents : Formula := .conj H0401 H0402

def comprehension : Derives [] graphExists := by
  apply Derives.delta1Comprehension (p := matrix (.var 152)) (q := matrix (.var 152)) 152 2 (.bounded (by decide)) (.bounded (by decide)) rfl (by decide) (by decide)
  exact .allI 152 rfl (.andI (.impI (.hypothesis List.mem_cons_self))
    (.impI (.hypothesis List.mem_cons_self)))

def decoded : Proof [] (.imp spec (.allN 150 (.allN 151
    (.imp (.member (pair (.var 150) (.var 151)) 2) (criterion (.var 150) (.var 151)))))) := by
  apply Proof.impI
  apply Proof.allI 150 (by decide)
  apply Proof.allI 151 (by decide)
  apply Proof.impI
  have hs : Proof [Formula.member (pair (.var 150) (.var 151)) 2, spec] spec := .hypothesis (List.mem_cons_of_mem _ List.mem_cons_self)
  have hm := Proof.impE (Proof.andL (Proof.allE 152 (pair (.var 150) (.var 151)) (by decide) hs)) hyp
  apply Proof.exBE 153 (.succ (pair (.var 150) (.var 151))) (by decide) (by decide) (by decide) hm
  apply Proof.exBE 154 (.succ (pair (.var 150) (.var 151))) (by decide) (by decide) (by decide) hyp
  let Δ : List Formula := [
    Formula.conj (Formula.eq (pair (.var 150) (.var 151)) (pair (.var 153) (.var 154)))
      (criterion (.var 153) (.var 154)),
    Formula.lt (.var 154) (.succ (pair (.var 150) (.var 151))),
    Formula.exB 154 (.succ (pair (.var 150) (.var 151)))
      (.conj (.eq (pair (.var 150) (.var 151)) (pair (.var 153) (.var 154))) (criterion (.var 153) (.var 154))),
    Formula.lt (.var 153) (.succ (pair (.var 150) (.var 151))),
    Formula.member (pair (.var 150) (.var 151)) 2, spec]
  have hraw : Proof Δ (.conj (.eq (pair (.var 150) (.var 151)) (pair (.var 153) (.var 154)))
      (criterion (.var 153) (.var 154))) := hyp
  have hp := pairInjectiveOpen (.var 150) (.var 151) (.var 153) (.var 154) (Proof.andL hraw)
  have hc := Proof.andR hraw
  have he := Proof.eqSubst (criterion (.var 153) (.var 161)) 161 (.var 154) (.var 151)
    (by decide) (by decide) (Proof.eqSymm (Proof.andR hp)) hc
  exact Proof.eqSubst (criterion (.var 161) (.var 151)) 161 (.var 153) (.var 150)
    (by decide) (by decide) (Proof.eqSymm (Proof.andL hp)) he

def encoded : Proof [] (.imp spec (.allN 150 (.allN 151
    (.imp (criterion (.var 150) (.var 151)) (.member (pair (.var 150) (.var 151)) 2))))) := by
  apply Proof.impI
  apply Proof.allI 150 (by decide)
  apply Proof.allI 151 (by decide)
  apply Proof.impI
  have hs : Proof [criterion (.var 150) (.var 151), spec] spec := .hypothesis (List.mem_cons_of_mem _ List.mem_cons_self)
  apply Proof.impE (Proof.andR (Proof.allE 152 (pair (.var 150) (.var 151)) (by decide) hs))
  apply Proof.exBI 153 (.succ (pair (.var 150) (.var 151))) (.var 150) (by decide) (firstProjectionBound _ _)
  apply Proof.exBI 154 (.succ (pair (.var 150) (.var 151))) (.var 151) (by decide) (secondProjectionBound _ _)
  exact .andI (eqRefl _) hyp

def zeroNotOne {Γ : List Formula} : Proof Γ (neg (.eq (.lit 0) (.lit 1))) := by
  apply Proof.impI
  have h01 : Proof (.eq (.lit 0) (.lit 1)::Γ) (.lt (.lit 0) (.lit 1)) :=
    .ltRewrite (eqRefl _) (ax (.symm (.literalSucc 0))) (ltSucc (.lit 0))
  exact .ltIrrefl (.ltRewrite hyp (eqRefl _) h01)
def zeroBelowTwo {Γ : List Formula} : Proof Γ (.lt (.lit 0) (.lit 2)) :=
  .ltRewrite (eqRefl _) (ax (.symm (.literalSucc 1)))
    (.leLtTrans (.zeroLe (.lit 1)) (ltSucc (.lit 1)))
def oneBelowTwo {Γ : List Formula} : Proof Γ (.lt (.lit 1) (.lit 2)) :=
  .ltRewrite (eqRefl _) (ax (.symm (.literalSucc 1))) (ltSucc (.lit 1))

def yesCriterion {Γ : List Formula} (j : Term) (h : Proof Γ (hit j)) :
    Proof Γ (criterion j (.lit 1)) :=
  .andI oneBelowTwo (.andI (.impI (push h)) (.impI (eqRefl _)))
def noCriterion {Γ : List Formula} (j : Term) (h : Proof Γ (neg (hit j))) :
    Proof Γ (criterion j (.lit 0)) :=
  .andI zeroBelowTwo (.andI (.impI (.botE (.impE zeroNotOne hyp)))
    (.impI (.botE (.impE (push h) hyp))))

def bitLeOne {Γ : List Formula} (e : Term) (h : Proof Γ (.lt e (.lit 2))) :
    Proof Γ (.le e (.lit 1)) :=
  DatosRecodificacionBetaRCA.belowSuccessor e (.lit 1)
    (.ltRewrite (eqRefl _) (ax (.literalSucc 1)) h)

example : (matrix (.var 152)).bounded = true := by decide
example : freshSet 2 [antecedents] = true := by decide
example : (matrix (.var 152)).setFree.all (· == 5) = true := by decide
example : spec.safe 152 (pair (.var 150) (.var 151)) = true := by decide
example : (matrix (.var 152)).safe 152 (.var 153) = false := by decide
example : spec.setFree.contains 2 = true := by decide
example : antecedents.setFree.contains 2 = false := by decide
#print axioms comprehension
#print axioms decoded
#print axioms encoded
#print axioms yesCriterion
#print axioms noCriterion
#print axioms bitLeOne
#eval ("M14_comprehension", ruleProfile comprehension)
#eval ("M14_decoded", profile decoded)
#eval ("M14_encoded", profile encoded)
end MatematicaAbierta.Continuo.GraficaBitsAcotadosRCA
