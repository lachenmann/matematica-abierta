import MatematicaAbierta.Continuo.SelectoresInternosRCA

/-! H04-04.g: derive BaseGraph and StepGraph from the NUMERIC trace
formula and the two selector equivalences. Neither property is assumed.
Uniform existence/extension of the numeric beta codes remains a separate
obligation. The graph equivalences will eventually be supplied by the M05
comprehensions; elimination of their set existentials is H04-04.h.
-/
namespace MatematicaAbierta.Continuo.PropiedadesTrazaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA

def prepend {Γ : List Formula} {p : Formula} (Δ : List Formula) (h : Proof Γ p) : Proof (Δ++Γ) p :=
  match Δ with
  | [] => h
  | _::ds => CalculoOrdenRCA.push (prepend ds h)

def constructionContext : List Formula := [finiteTraceMatrix,originalSpec .d,originalSpec .u]
def baseContext : List Formula :=
  [oldGraphs (.lit 0) (.var 1) (.var 2), .lt (.var 2) valueBound,.lt (.var 1) valueBound] ++ constructionContext

def baseFromTrace : Proof constructionContext baseGraph := by
  apply Proof.allBI 1 valueBound (by decide) rfl
  apply Proof.allBI 2 valueBound (by decide) rfl
  apply Proof.impI
  have ht : Proof baseContext finiteTraceMatrix := push (push (push hyp))
  have hsu : Proof baseContext (originalSpec .u) := push (push (push (push (push hyp))))
  have hsd : Proof baseContext (originalSpec .d) := push (push (push (push hyp)))
  have nu := Proof.impE (closed (renameSpecification .u)) hsu
  have nd := Proof.impE (closed (renameSpecification .d)) hsd
  have hu := Proof.impE (Proof.impE (closed (decodeGraph .u .zero .u)) nu) (Proof.andL hyp)
  have hd := Proof.impE (Proof.impE (closed (decodeGraph .d .zero .d)) nd) (Proof.andR hyp)
  have hu0 := Proof.andL (Proof.andR ht)
  have hd1 := Proof.andL (Proof.andR (Proof.andR ht))
  exact .andI
    (.impE (.impE (closed (betaSpecialized .u .zero .u .zero)) (.andR (.andR hu))) hu0)
    (.impE (.impE (closed (betaSpecialized .d .zero .d .one)) (.andR (.andR hd))) hd1)

def stepContext : List Formula :=
  [oldGraphs (.succ (.var 0)) (.var 1) (.var 2), .lt (.var 2) valueBound,
   .lt (.var 1) valueBound] ++ constructionContext
def rawLeaf : Formula := .conj (recurrenceValues (.var 0)) (traceValueRelations (.var 0))
def renamedLeaf : Formula := (rawLeaf.subst 1 (.var 18)).subst 2 (.var 19)
def leafPrefix : List Formula :=
  [renamedLeaf,.lt (.var 19) valueBound,
   .exB 2 valueBound (rawLeaf.subst 1 (.var 18)), .lt (.var 18) valueBound,
   .exB 1 valueBound (.exB 2 valueBound rawLeaf), .lt (.var 7) (.lit 2),
   .exB 7 (.lit 2) (.exB 1 valueBound (.exB 2 valueBound rawLeaf)), .lt (.var 6) valueBound,
   .exB 6 valueBound (.exB 7 (.lit 2) (.exB 1 valueBound (.exB 2 valueBound rawLeaf))),
   .lt (.var 5) valueBound]
def leafContext : List Formula := leafPrefix ++ stepContext

def leafToStep
    (nu : Proof stepContext (namedSpec .u)) (nd : Proof stepContext (namedSpec .d))
    (hu : Proof stepContext (reading .u .successor .u))
    (hd : Proof stepContext (reading .d .successor .d)) :
    Proof leafContext (stepExistentials (.var 0)) := by
  have hw : Proof leafContext renamedLeaf := hyp
  have hu' := prepend leafPrefix hu
  have hd' := prepend leafPrefix hd
  have nU := prepend leafPrefix nu
  have nD := prepend leafPrefix nd
  have hk : Proof leafContext (.le (.var 0) stageBound) :=
    .leTrans (leSucc (.var 0)) (.andL hu')
  have hbU : Proof leafContext (beta (.var 8) (.var 9) (.var 0) (.var 5)) :=
    .andL (.andR hw)
  have hbD : Proof leafContext (beta (.var 10) (.var 11) (.var 0) (.var 6)) :=
    .andL (.andR (.andR hw))
  have hbUn : Proof leafContext (beta (.var 8) (.var 9) (.succ (.var 0)) (.var 18)) :=
    .andL (.andR (.andR (.andR hw)))
  have hbDn : Proof leafContext (beta (.var 10) (.var 11) (.succ (.var 0)) (.var 19)) :=
    .andR (.andR (.andR (.andR hw)))
  have hvU : Proof leafContext (.eq (.var 1) (.var 18)) :=
    .impE (.impE (closed (betaSpecialized .u .successor .u .traceU)) (.andR (.andR hu'))) hbUn
  have hvD : Proof leafContext (.eq (.var 2) (.var 19)) :=
    .impE (.impE (closed (betaSpecialized .d .successor .d .traceD)) (.andR (.andR hd'))) hbDn
  have h5 : Proof leafContext (.lt (.var 5) valueBound) :=
    push (push (push (push (push (push (push (push (push hyp))))))))
  have h6 : Proof leafContext (.lt (.var 6) valueBound) :=
    push (push (push (push (push (push (push hyp))))))
  have h7 : Proof leafContext (.lt (.var 7) (.lit 2)) := push (push (push (push (push hyp))))
  have gU := Proof.impE (Proof.impE (closed (encodeGraph .u .current .oldU)) nU)
    (Proof.andI hk (Proof.andI h5 hbU))
  have gD := Proof.impE (Proof.impE (closed (encodeGraph .d .current .oldD)) nD)
    (Proof.andI hk (Proof.andI h6 hbD))
  apply Proof.exBI 5 valueBound (.var 5) (by decide) h5
  apply Proof.exBI 6 valueBound (.var 6) (by decide) h6
  apply Proof.exBI 7 (.lit 2) (.var 7) (by decide) h7
  exact .andI (.andI gU gD)
    (.andI (.andL (.andL hw))
      (.andI (.eqTrans hvU (.andL (.andR (.andL hw))))
        (.andI (.eqTrans hvD (.andL (.andR (.andR (.andL hw)))))
          (.andR (.andR (.andR (.andL hw)))))))

def stepFromTrace : Proof constructionContext stepGraph := by
  apply Proof.allI 0 (by decide)
  apply Proof.allBI 1 valueBound (by decide) rfl
  apply Proof.allBI 2 valueBound (by decide) rfl
  apply Proof.impI
  have ht : Proof stepContext finiteTraceMatrix := push (push (push hyp))
  have hsu : Proof stepContext (originalSpec .u) := push (push (push (push (push hyp))))
  have hsd : Proof stepContext (originalSpec .d) := push (push (push (push hyp)))
  have nu := Proof.impE (closed (renameSpecification .u)) hsu
  have nd := Proof.impE (closed (renameSpecification .d)) hsd
  have hu := Proof.impE (Proof.impE (closed (decodeGraph .u .successor .u)) nu) (Proof.andL hyp)
  have hd := Proof.impE (Proof.impE (closed (decodeGraph .d .successor .d)) nd) (Proof.andR hyp)
  have hfinite := Proof.andR (Proof.andR (Proof.andR ht))
  have hs : Proof stepContext (finiteTraceStep (.var 0)) :=
    .allBE 0 stageBound (.var 0) (by decide) hfinite (.succLeLt (.andL hu))
  apply Proof.exBE 5 valueBound (by decide) (by decide) rfl hs
  apply Proof.exBE 6 valueBound (by decide) (by decide) rfl hyp
  apply Proof.exBE 7 (.lit 2) (by decide) (by decide) rfl hyp
  apply Proof.exBErename 1 18 valueBound (by decide) (by decide) rfl (by decide) hyp
  apply Proof.exBErename 2 19 valueBound (by decide) (by decide) rfl (by decide) hyp
  exact leafToStep nu nd hu hd

def traceToGraphProperties : Proof []
    (.imp (originalSpec .u) (.imp (originalSpec .d)
      (.imp finiteTraceMatrix (.conj baseGraph stepGraph)))) :=
  .impI (.impI (.impI (.andI baseFromTrace stepFromTrace)))

def invariantFromTrace : Proof constructionContext (.allN 0 (guardedInvariant (.var 0))) :=
  .impE (.impE (closed (.embed guardedGraphTheorem)) baseFromTrace) stepFromTrace
def traceToInduction : Proof []
    (.imp (originalSpec .u) (.imp (originalSpec .d)
      (.imp finiteTraceMatrix (.allN 0 (guardedInvariant (.var 0)))))) :=
  .impI (.impI (.impI invariantFromTrace))

/-- H04-04.e: each selector graph is single-valued, derived from pairing
decoding and beta uniqueness. No totality or numeric code existence follows. -/
def graphSingleValued (c : Channel) : Proof []
    (.imp (originalSpec c) (.allN 0 (.allN 1 (.allN 2
      (.imp (.conj (.member (pair (.var 0) (.var 1)) (graphSet c))
          (.member (pair (.var 0) (.var 2)) (graphSet c)))
        (.eq (.var 1) (.var 2))))))) := by
  apply Proof.impI
  apply Proof.allI 0 (by cases c <;> decide)
  apply Proof.allI 1 (by cases c <;> decide)
  apply Proof.allI 2 (by cases c <;> decide)
  apply Proof.impI
  have hs : Proof
      [.conj (.member (pair (.var 0) (.var 1)) (graphSet c))
        (.member (pair (.var 0) (.var 2)) (graphSet c)),originalSpec c] (originalSpec c) := push hyp
  have hn := Proof.impE (closed (renameSpecification c)) hs
  have hu := Proof.impE (Proof.impE (closed (decodeGraph c .current .u)) hn) (Proof.andL hyp)
  have hv := Proof.impE (Proof.impE (closed (decodeGraph c .current .d)) hn) (Proof.andR hyp)
  have he : Proof
      [.conj (.member (pair (.var 0) (.var 1)) (graphSet c))
        (.member (pair (.var 0) (.var 2)) (graphSet c)),originalSpec c]
      (.imp (beta (codeA c) (codeB c) (.var 0) (.var 1))
        (.imp (beta (codeA c) (codeB c) (.var 0) (.var 2)) (.eq (.var 1) (.var 2)))) := by
    let a := codeA c
    let b := codeB c
    cases c <;> exact Proof.allE 19 (.var 2) (by decide)
      (Proof.allE 18 (.var 1) (by decide)
        (Proof.allE 0 (.var 0) (by decide)
          (Proof.allE 9 b (by decide)
            (Proof.allE 8 a (by decide) (closed betaUniqueFresh)))))
  exact .impE (.impE he (.andR (.andR hu))) (.andR (.andR hv))

#print axioms baseFromTrace
#print axioms stepFromTrace
#print axioms traceToGraphProperties
#print axioms traceToInduction
#print axioms graphSingleValued
#eval ("trace_to_graphs", profile traceToGraphProperties)
#eval ("trace_to_guarded_induction", profile traceToInduction)
end MatematicaAbierta.Continuo.PropiedadesTrazaRCA
