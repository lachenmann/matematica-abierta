import MatematicaAbierta.Continuo.PropiedadesTrazaRCA

/-! H04-04.e: total bounded beta readings and graph totality FROM an
existing finite numeric trace. A real bounded IΣ₁ instance is used. The
free T is the trace's common bound; uniform existence of T/codes is NOT
proved or assumed as a theory axiom. -/
namespace MatematicaAbierta.Continuo.TotalidadTrazaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA

def totalReadings (k : Term) : Formula :=
  .exB 1 valueBound (.exB 2 valueBound
    (.conj (beta (.var 8) (.var 9) k (.var 1))
      (beta (.var 10) (.var 11) k (.var 2))))
def totalGuard (k : Term) : Formula := .imp (.le k stageBound) (totalReadings k)

def totalBase : Proof [finiteTraceMatrix] (totalGuard (.lit 0)) := by
  apply Proof.impI
  have ht : Proof [.le (.lit 0) stageBound,finiteTraceMatrix] finiteTraceMatrix := push hyp
  have h1 := Proof.andL ht
  have h0 : Proof [.le (.lit 0) stageBound,finiteTraceMatrix] (.lt (.lit 0) valueBound) :=
    .ltTrans (.embed ConstruccionBaseTrazaRCA.zeroLtOne) h1
  apply Proof.exBI 1 valueBound (.lit 0) (by decide) h0
  apply Proof.exBI 2 valueBound (.lit 1) (by decide) h1
  exact .andI (.andL (.andR ht)) (.andL (.andR (.andR ht)))

def totalStepContext : List Formula :=
  [.le (.succ (.var 0)) stageBound,totalGuard (.var 0),finiteTraceMatrix]
def totalLeafPrefix : List Formula :=
  [PropiedadesTrazaRCA.rawLeaf,.lt (.var 2) valueBound,
   .exB 2 valueBound PropiedadesTrazaRCA.rawLeaf,.lt (.var 1) valueBound,
   .exB 1 valueBound (.exB 2 valueBound PropiedadesTrazaRCA.rawLeaf),.lt (.var 7) (.lit 2),
   .exB 7 (.lit 2) (.exB 1 valueBound (.exB 2 valueBound PropiedadesTrazaRCA.rawLeaf)),.lt (.var 6) valueBound,
   .exB 6 valueBound (.exB 7 (.lit 2) (.exB 1 valueBound (.exB 2 valueBound PropiedadesTrazaRCA.rawLeaf))),
   .lt (.var 5) valueBound]
def totalLeaf : Proof (totalLeafPrefix ++ totalStepContext) (totalReadings (.succ (.var 0))) := by
  have hw : Proof (totalLeafPrefix ++ totalStepContext) PropiedadesTrazaRCA.rawLeaf := hyp
  have h1 : Proof (totalLeafPrefix ++ totalStepContext) (.lt (.var 1) valueBound) := push (push (push hyp))
  have h2 : Proof (totalLeafPrefix ++ totalStepContext) (.lt (.var 2) valueBound) := push hyp
  apply Proof.exBI 1 valueBound (.var 1) (by decide) h1
  apply Proof.exBI 2 valueBound (.var 2) (by decide) h2
  exact .andI (.andL (.andR (.andR (.andR hw)))) (.andR (.andR (.andR (.andR hw))))

def totalStep : Proof [finiteTraceMatrix]
    (.allN 0 (.imp (totalGuard (.var 0)) (totalGuard (.succ (.var 0))))) := by
  apply Proof.allI 0 (by decide)
  apply Proof.impI
  apply Proof.impI
  have ht : Proof totalStepContext finiteTraceMatrix := push (push hyp)
  have hs : Proof totalStepContext (finiteTraceStep (.var 0)) :=
    .allBE 0 stageBound (.var 0) (by decide) (.andR (.andR (.andR ht))) (.succLeLt hyp)
  apply Proof.exBE 5 valueBound (by decide) (by decide) rfl hs
  apply Proof.exBE 6 valueBound (by decide) (by decide) rfl hyp
  apply Proof.exBE 7 (.lit 2) (by decide) (by decide) rfl hyp
  apply Proof.exBE 1 valueBound (by decide) (by decide) rfl hyp
  apply Proof.exBE 2 valueBound (by decide) (by decide) rfl hyp
  exact totalLeaf

def totalByInduction : Proof [finiteTraceMatrix] (.allN 0 (totalGuard (.var 0))) :=
  .sigma1Induction 0 (.bounded rfl) (by decide) (by decide) (by decide) totalBase totalStep
def traceTotal : Proof [] (.imp finiteTraceMatrix (.allN 0 (totalGuard (.var 0)))) :=
  .impI totalByInduction

def totalGraphs (k : Term) : Formula :=
  .exB 1 valueBound (.exB 2 valueBound (oldGraphs k (.var 1) (.var 2)))
def graphTotalContext : List Formula :=
  [.le (.var 0) stageBound] ++ PropiedadesTrazaRCA.constructionContext
def graphTotalLeafContext : List Formula :=
  [.conj (beta (.var 8) (.var 9) (.var 0) (.var 1)) (beta (.var 10) (.var 11) (.var 0) (.var 2)),
   .lt (.var 2) valueBound,.exB 2 valueBound
     (.conj (beta (.var 8) (.var 9) (.var 0) (.var 1)) (beta (.var 10) (.var 11) (.var 0) (.var 2))),
   .lt (.var 1) valueBound] ++ graphTotalContext

def graphTotalLeaf : Proof graphTotalLeafContext (totalGraphs (.var 0)) := by
  have hb : Proof graphTotalLeafContext
      (.conj (beta (.var 8) (.var 9) (.var 0) (.var 1)) (beta (.var 10) (.var 11) (.var 0) (.var 2))) := hyp
  have hk : Proof graphTotalLeafContext (.le (.var 0) stageBound) := push (push (push (push hyp)))
  have h1 : Proof graphTotalLeafContext (.lt (.var 1) valueBound) := push (push (push hyp))
  have h2 : Proof graphTotalLeafContext (.lt (.var 2) valueBound) := push hyp
  have su : Proof graphTotalLeafContext (originalSpec .u) := push (push (push (push (push (push (push hyp))))))
  have sd : Proof graphTotalLeafContext (originalSpec .d) := push (push (push (push (push (push hyp)))))
  have nu := Proof.impE (closed (renameSpecification .u)) su
  have nd := Proof.impE (closed (renameSpecification .d)) sd
  have gu := Proof.impE (Proof.impE (closed (encodeGraph .u .current .u)) nu)
    (Proof.andI hk (Proof.andI h1 (Proof.andL hb)))
  have gd := Proof.impE (Proof.impE (closed (encodeGraph .d .current .d)) nd)
    (Proof.andI hk (Proof.andI h2 (Proof.andR hb)))
  apply Proof.exBI 1 valueBound (.var 1) (by decide) h1
  apply Proof.exBI 2 valueBound (.var 2) (by decide) h2
  exact .andI gu gd

def graphTotalFromTrace : Proof PropiedadesTrazaRCA.constructionContext
    (.allN 0 (.imp (.le (.var 0) stageBound) (totalGraphs (.var 0)))) := by
  apply Proof.allI 0 (by decide)
  apply Proof.impI
  have ht : Proof graphTotalContext finiteTraceMatrix := push hyp
  have total : Proof graphTotalContext (.allN 0 (totalGuard (.var 0))) :=
    .impE (closed traceTotal) ht
  have hg : Proof graphTotalContext (totalReadings (.var 0)) :=
    .impE (.allE 0 (.var 0) (by decide) total) hyp
  apply Proof.exBE 1 valueBound (by decide) (by decide) rfl hg
  apply Proof.exBE 2 valueBound (by decide) (by decide) rfl hyp
  exact graphTotalLeaf
def traceGraphTotal : Proof []
    (.imp (originalSpec .u) (.imp (originalSpec .d) (.imp finiteTraceMatrix
      (.allN 0 (.imp (.le (.var 0) stageBound) (totalGraphs (.var 0))))))) :=
  .impI (.impI (.impI graphTotalFromTrace))

#print axioms totalByInduction
#print axioms traceTotal
#print axioms traceGraphTotal
#eval ("trace_total_readings", profile traceTotal)
#eval ("trace_total_graphs", profile traceGraphTotal)
end MatematicaAbierta.Continuo.TotalidadTrazaRCA
