import MatematicaAbierta.Continuo.LogicaClasicaOrdinariaRCA

/-! M14/H04-03: graph exactness, total admissible bits, uniqueness and M13 use.
H04-01/H04-02 are retained as explicit antecedents; finite search itself works
for any relation. Classical cases are explicit in the M14 proof profile. -/
namespace MatematicaAbierta.Continuo.ContratoBitsAdmisiblesRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA GraficaBitsAcotadosRCA
abbrev CProof := LogicaClasicaOrdinariaRCA.Proof

def oldClosed {Γ : List Formula} {p : Formula} (h : Proof [] p) : Proof Γ p :=
  .weaken (fun _ hm => False.elim (List.not_mem_nil hm)) h

def fact (j e : Term) : Formula := .conj (.member (pair j e) 2)
  (.conj (.le e (.lit 1)) (criterion j e))
def total : Formula := .allN 150 (.exN 7 (fact (.var 150) (.var 7)))

def encodeYes : Proof [hit (.var 150),spec] (fact (.var 150) (.lit 1)) := by
  have hs : Proof [hit (.var 150),spec] spec := .hypothesis (List.mem_cons_of_mem _ List.mem_cons_self)
  have hc : Proof [hit (.var 150),spec] (criterion (.var 150) (.lit 1)) := yesCriterion _ hyp
  have he := Proof.impE (oldClosed encoded) hs
  have he1 := Proof.allE 150 (.var 150) (by decide) he
  have he2 := Proof.allE 151 (.lit 1) (by decide) he1
  exact .andI (.impE he2 hc) (.andI (leRefl _) hc)
def encodeNo : Proof [neg (hit (.var 150)),spec] (fact (.var 150) (.lit 0)) := by
  have hs : Proof [neg (hit (.var 150)),spec] spec := .hypothesis (List.mem_cons_of_mem _ List.mem_cons_self)
  have hc : Proof [neg (hit (.var 150)),spec] (criterion (.var 150) (.lit 0)) := noCriterion _ hyp
  have he := Proof.impE (oldClosed encoded) hs
  have he1 := Proof.allE 150 (.var 150) (by decide) he
  have he2 := Proof.allE 151 (.lit 0) (by decide) he1
  exact .andI (.impE he2 hc) (.andI (.zeroLe _) hc)
def totalFromSpec : CProof [] (.imp spec total) := by
  apply LogicaClasicaOrdinariaRCA.Proof.impI
  apply LogicaClasicaOrdinariaRCA.Proof.allI 150 (by decide)
  apply LogicaClasicaOrdinariaRCA.Proof.cases (p := hit (.var 150))
  · exact .exNI 7 (.lit 1) (by decide) (LogicaClasicaOrdinariaRCA.old encodeYes)
  · exact .exNI 7 (.lit 0) (by decide) (LogicaClasicaOrdinariaRCA.old encodeNo)

def belowOneZero {Γ : List Formula} (e : Term) (h : Proof Γ (.lt e (.lit 1))) : Proof Γ (.eq e (.lit 0)) :=
  .leAntisymm (DatosRecodificacionBetaRCA.belowSuccessor e (.lit 0)
    (.ltRewrite (eqRefl _) (ax (.literalSucc 0)) h)) (.zeroLe _)
def uniqueCriterion {Γ : List Formula} (j e d : Term)
    (hc : Proof Γ (criterion j e)) (hd : Proof Γ (criterion j d)) : Proof Γ (.eq e d) := by
  apply Proof.orderCases e (.lit 1)
  · have he0 : Proof (.lt e (.lit 1)::Γ) (.eq e (.lit 0)) := belowOneZero e hyp
    apply Proof.orderCases d (.lit 1)
    · exact .eqTrans (push he0) (.eqSymm (belowOneZero d hyp))
    · have hd1 : Proof (.eq d (.lit 1)::.lt e (.lit 1)::Γ) (.eq d (.lit 1)) := hyp
      have hh : Proof (.eq d (.lit 1)::.lt e (.lit 1)::Γ) (hit j) :=
        .impE (.andL (.andR (push (push hd)))) hd1
      have he1 : Proof (.eq d (.lit 1)::.lt e (.lit 1)::Γ) (.eq e (.lit 1)) :=
        .impE (.andR (.andR (push (push hc)))) hh
      exact .botE (.impE zeroNotOne (.eqTrans (.eqSymm (push he0)) he1))
    · exact .botE (.ltIrrefl (.ltLeTrans hyp (push (push (bitLeOne d (.andL hd))))))
  · have he1 : Proof (.eq e (.lit 1)::Γ) (.eq e (.lit 1)) := hyp
    have hh : Proof (.eq e (.lit 1)::Γ) (hit j) := .impE (.andL (.andR (push hc))) he1
    have hd1 : Proof (.eq e (.lit 1)::Γ) (.eq d (.lit 1)) := .impE (.andR (.andR (push hd))) hh
    exact .eqTrans he1 (.eqSymm hd1)
  · exact .botE (.ltIrrefl (.ltLeTrans hyp (push (bitLeOne e (.andL hc)))))

def zeroCharacterisation {Γ : List Formula} (j e : Term) (hc : Proof Γ (criterion j e)) :
    Proof Γ (iffF (.eq e (.lit 0)) (neg (hit j))) := by
  apply Proof.andI
  · apply Proof.impI
    apply Proof.impI
    have hh : Proof (hit j :: Formula.eq e (.lit 0)::Γ) (hit j) := hyp
    have he1 : Proof (hit j :: Formula.eq e (.lit 0)::Γ) (.eq e (.lit 1)) :=
      .impE (.andR (.andR (push (push hc)))) hh
    have he0 : Proof (hit j :: Formula.eq e (.lit 0)::Γ) (.eq e (.lit 0)) := push hyp
    exact .impE zeroNotOne (.eqTrans (.eqSymm he0) he1)
  · apply Proof.impI
    apply Proof.orderCases e (.lit 1)
    · exact belowOneZero e hyp
    · have he1 : Proof (Formula.eq e (.lit 1)::neg (hit j)::Γ) (.eq e (.lit 1)) := hyp
      have hh : Proof (Formula.eq e (.lit 1)::neg (hit j)::Γ) (hit j) :=
        .impE (.andL (.andR (push (push hc)))) he1
      have hn : Proof (Formula.eq e (.lit 1)::neg (hit j)::Γ) (neg (hit j)) := push hyp
      exact .botE (.impE hn hh)
    · exact .botE (.ltIrrefl (.ltLeTrans hyp (push (push (bitLeOne e (.andL hc))))))

def uniqueness : Formula := .allN 150 (.allN 151 (.allN 162
  (.imp (.conj (.member (pair (.var 150) (.var 151)) 2) (.member (pair (.var 150) (.var 162)) 2))
    (.eq (.var 151) (.var 162)))))
def uniqueFromSpec : Proof [] (.imp spec uniqueness) := by
  apply Proof.impI
  apply Proof.allI 150 (by decide)
  apply Proof.allI 151 (by decide)
  apply Proof.allI 162 (by decide)
  apply Proof.impI
  have hs : Proof [Formula.conj (Formula.member (pair (.var 150) (.var 151)) 2)
      (Formula.member (pair (.var 150) (.var 162)) 2),spec] spec := .hypothesis (List.mem_cons_of_mem _ List.mem_cons_self)
  have h0 := Proof.impE (oldClosed decoded) hs
  have hj := Proof.allE 150 (.var 150) (by decide) h0
  have h1 := Proof.allE 151 (.var 151) (by decide) hj
  have h2 := Proof.allE 151 (.var 162) (by decide) hj
  exact uniqueCriterion _ _ _ (.impE h1 (.andL hyp)) (.impE h2 (.andR hyp))

def body : Formula := .conj spec (.conj total uniqueness)
def contract : Formula := .imp antecedents (.exS 2 body)
def admissibleGraph : CProof [] contract := by
  apply LogicaClasicaOrdinariaRCA.Proof.impI
  have hs : CProof [antecedents] graphExists :=
    LogicaClasicaOrdinariaRCA.closed (LogicaClasicaOrdinariaRCA.old (.embed comprehension))
  apply LogicaClasicaOrdinariaRCA.Proof.exSE 2 (by decide) (by decide) hs
  apply LogicaClasicaOrdinariaRCA.Proof.exSI 2
  exact .andI LogicaClasicaOrdinariaRCA.hyp
    (.andI (.impE (LogicaClasicaOrdinariaRCA.closed totalFromSpec) LogicaClasicaOrdinariaRCA.hyp)
      (.impE (LogicaClasicaOrdinariaRCA.closed (LogicaClasicaOrdinariaRCA.old uniqueFromSpec)) LogicaClasicaOrdinariaRCA.hyp))

def H0403 : CProof [] (.allN 156 contract) :=
  .allI 156 rfl admissibleGraph

open ContratoExtensionBetaRCA

def traceCore : Formula := .conj finiteTraceMatrix
  (.conj (.lt (.var 1) (.var 4)) (.conj (.lt (.var 2) (.var 4))
    (.conj (beta (.var 8) (.var 9) (.var 3) (.var 1))
      (beta (.var 10) (.var 11) (.var 3) (.var 2)))))
def suppliedExtension : Formula := .exN 7 (.conj (fact (.var 3) (.var 7)) extensionExists)
def extensionFromBits : CProof [] (.imp (.conj spec traceCore) suppliedExtension) := by
  apply LogicaClasicaOrdinariaRCA.Proof.impI
  have hs : CProof [Formula.conj spec traceCore] spec := .andL LogicaClasicaOrdinariaRCA.hyp
  have ht := LogicaClasicaOrdinariaRCA.Proof.impE
    (LogicaClasicaOrdinariaRCA.closed totalFromSpec) hs
  have hk := LogicaClasicaOrdinariaRCA.Proof.allE 150 (.var 3) (by decide) ht
  apply LogicaClasicaOrdinariaRCA.Proof.exNE 7 (by decide) (by decide) hk
  have hf : CProof [fact (.var 3) (.var 7),Formula.conj spec traceCore] (fact (.var 3) (.var 7)) := LogicaClasicaOrdinariaRCA.hyp
  have hc : CProof [fact (.var 3) (.var 7),Formula.conj spec traceCore] traceCore :=
    .andR (.hypothesis (List.mem_cons_of_mem _ List.mem_cons_self))
  have hi : CProof [fact (.var 3) (.var 7),Formula.conj spec traceCore] extensionInput :=
    .andI (.andL hc) (.andI (.andL (.andR hc)) (.andI (.andL (.andR (.andR hc)))
      (.andI (.andL (.andR (.andR (.andR hc))))
        (.andI (.andR (.andR (.andR (.andR hc)))) (.andI (.andL hf) (.andL (.andR hf)))))))
  have h0 := LogicaClasicaOrdinariaRCA.Proof.allE 3 (.var 3) (by decide)
    (LogicaClasicaOrdinariaRCA.closed (Γ := [fact (.var 3) (.var 7),Formula.conj spec traceCore]) (.embed ContratoExtensionCompletoRCA.numericExtension))
  have h1 := LogicaClasicaOrdinariaRCA.Proof.allE 4 (.var 4) (by decide) h0
  have h2 := LogicaClasicaOrdinariaRCA.Proof.allE 8 (.var 8) (by decide) h1
  have h3 := LogicaClasicaOrdinariaRCA.Proof.allE 9 (.var 9) (by decide) h2
  have h4 := LogicaClasicaOrdinariaRCA.Proof.allE 10 (.var 10) (by decide) h3
  have h5 := LogicaClasicaOrdinariaRCA.Proof.allE 11 (.var 11) (by decide) h4
  have h6 := LogicaClasicaOrdinariaRCA.Proof.allE 1 (.var 1) (by decide) h5
  have h7 := LogicaClasicaOrdinariaRCA.Proof.allE 2 (.var 2) (by decide) h6
  have h8 := LogicaClasicaOrdinariaRCA.Proof.allE 7 (.var 7) (by decide) h7
  exact .exNI 7 (.var 7) (by decide) (.andI hf (.impE h8 hi))

example : traceCore.numFree.contains 7 = false := by decide
example : suppliedExtension.numFree.contains 7 = false := by decide
example : freshNum 7 [Formula.conj spec traceCore] = true := by decide
example : (Formula.conj (fact (.var 3) (.var 7)) extensionExists).safe 7 (.var 7) = true := by decide
example : extensionInput.setFree.all (· == 2) = true := by decide
#print axioms extensionFromBits
#eval ("M14_M13_incorporation", LogicaClasicaOrdinariaRCA.profile extensionFromBits)

example : contract.setFree.all (· == 5) = true := by decide
example : total.numFree.all (· == 156) = true := by decide
example : freshNum 7 [spec] = true := by decide
example : (fact (.var 150) (.var 7)).safe 7 (.lit 1) = true := by decide
example : freshSet 2 [antecedents] = true := by decide
example : (Formula.exS 2 body).setFree.contains 2 = false := by decide
#print axioms encodeYes
#print axioms encodeNo
#print axioms totalFromSpec
#print axioms zeroCharacterisation
#print axioms uniqueCriterion
#print axioms uniqueFromSpec
#print axioms H0403
#print axioms admissibleGraph
#eval ("M14_total", LogicaClasicaOrdinariaRCA.profile totalFromSpec)
#eval ("M14_unique", CalculoOrdenRCA.profile uniqueFromSpec)
#eval ("M14_H0403", LogicaClasicaOrdinariaRCA.profile admissibleGraph)
end MatematicaAbierta.Continuo.ContratoBitsAdmisiblesRCA
