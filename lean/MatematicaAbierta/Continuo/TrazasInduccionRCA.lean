import MatematicaAbierta.Continuo.CalculoRCA

/-!
H04-04: bounded β-code relations and actual Δ₁-comprehension instances.
H04-06: a closed INTERNAL implication BaseGraph → StepGraph → ∀k A(k),
whose proof tree uses the guarded IΣ₁ rule on the bounded graph formula.
Existence of uniform finite β-codes, a common value bound, remainder uniqueness,
and derivation of BaseGraph/StepGraph from those codes remain open.
-/
namespace MatematicaAbierta.Continuo.TrazasInduccionRCA
open CalculoRCA

def pair (k v : Term) : Term := .add (.mul (.add k v) (.add k v)) k
def gu (k v : Term) : Formula := .member (pair k v) 0
def gd (k v : Term) : Formula := .member (pair k v) 1
def gb (k v : Term) : Formula := .member (pair k v) 2
def valueBound : Term := .var 4
def stageBound : Term := .var 3

/-- q is named 12, away from all actual code/stage/value parameters below.
Only +, ×, comparisons and bounded quantification occur; no division symbol. -/
def beta (a b k v : Term) : Formula :=
  let modulus := Term.add (.lit 1) (.mul (.add k (.lit 1)) b)
  .conj (.lt v modulus)
    (.exB 12 (.succ a) (.eq a (.add (.mul (.var 12) modulus) v)))

/-- Numeric codes use names 8,9 for U and 10,11 for D. -/
def graphMatrix (a b : Term) : Formula :=
  .exB 1 (.succ (.var 0)) (.exB 2 (.succ (.var 0))
    (.conj (.eq (.var 0) (pair (.var 1) (.var 2)))
      (.conj (.le (.var 1) stageBound)
        (.conj (.lt (.var 2) valueBound) (beta a b (.var 1) (.var 2))))))

def numeratorGraphMatrix : Formula := graphMatrix (.var 8) (.var 9)
def denominatorGraphMatrix : Formula := graphMatrix (.var 10) (.var 11)

def hyp0 {Γ : List Formula} {p : Formula} : Derives (p::Γ) p :=
  .hypothesis (List.mem_cons_self)

def push {Γ : List Formula} {p q : Formula} (h : Derives Γ p) : Derives (q::Γ) p :=
  .weaken (fun _ hm => List.mem_cons_of_mem _ hm) h

/-- Genuine instances of the RCA₀ Δ₁ scheme. The two presentations are the
same Δ₀ matrix; their equivalence is derived by implication introduction. -/
def numeratorGraphExists : Derives []
    (.exS 0 (.allN 0 (iffF (.member (.var 0) 0) numeratorGraphMatrix))) :=
  .delta1Comprehension 0 0 (.bounded rfl) (.bounded rfl) rfl rfl rfl
    (.allI 0 rfl (.andI (.impI hyp0) (.impI hyp0)))

def denominatorGraphExists : Derives []
    (.exS 1 (.allN 0 (iffF (.member (.var 0) 1) denominatorGraphMatrix))) :=
  .delta1Comprehension 0 1 (.bounded rfl) (.bounded rfl) rfl rfl rfl
    (.allI 0 rfl (.andI (.impI hyp0) (.impI hyp0)))

def oldGraphs (k u d : Term) : Formula := .conj (gu k u) (gd k d)

/-- Stronger than the written M04 k≤K-guarded candidate: finite graphs are
empty outside their coded domain. No total function U or D is added to syntax. -/
def graphInvariant (k : Term) : Formula :=
  .allB 1 valueBound (.allB 2 valueBound
    (.imp (oldGraphs k (.var 1) (.var 2)) (invariant (.var 1) (.var 2))))

def baseGraph : Formula :=
  .allB 1 valueBound (.allB 2 valueBound
    (.imp (oldGraphs (.lit 0) (.var 1) (.var 2))
      (.conj (.eq (.var 1) (.lit 0)) (.eq (.var 2) (.lit 1)))))

def recurrenceValues (k : Term) : Formula :=
  .conj (gb k (.var 7))
    (.conj (.eq (.var 1) (.add (.mul (.lit 4) (.var 5)) (.mul (.lit 2) (.var 7))))
      (.conj (.eq (.var 2) (.mul (.lit 4) (.var 6))) (.le (.var 7) (.lit 1))))

def stepWitness (k : Term) : Formula :=
  .conj (oldGraphs k (.var 5) (.var 6)) (recurrenceValues k)

def stepExistentials (k : Term) : Formula :=
  .exB 5 valueBound (.exB 6 valueBound (.exB 7 (.lit 2) (stepWitness k)))

def stepGraph : Formula :=
  .allN 0 (.allB 1 valueBound (.allB 2 valueBound
    (.imp (oldGraphs (.succ (.var 0)) (.var 1) (.var 2)) (stepExistentials (.var 0)))))

def traceContext : List Formula := [stepGraph, baseGraph]

def baseInvariant : Derives traceContext (graphInvariant (.lit 0)) := by
  apply Derives.allBI 1 valueBound (by decide) rfl
  apply Derives.allBI 2 valueBound (by decide) rfl
  apply Derives.impI
  have hbase : Derives
      [oldGraphs (.lit 0) (.var 1) (.var 2), .lt (.var 2) valueBound,
        .lt (.var 1) valueBound, stepGraph, baseGraph] baseGraph :=
    push (push (push (push hyp0)))
  have hu : Derives
      [oldGraphs (.lit 0) (.var 1) (.var 2), .lt (.var 2) valueBound,
        .lt (.var 1) valueBound, stepGraph, baseGraph] (.lt (.var 1) valueBound) :=
    push (push hyp0)
  have hd : Derives
      [oldGraphs (.lit 0) (.var 1) (.var 2), .lt (.var 2) valueBound,
        .lt (.var 1) valueBound, stepGraph, baseGraph] (.lt (.var 2) valueBound) := push hyp0
  have he := Derives.impE
    (Derives.allBE 2 valueBound (.var 2) (by decide)
      (Derives.allBE 1 valueBound (.var 1) (by decide) hbase hu) hd) hyp0
  exact .leRewrite
    (.eqAdd (.eqMul (.arithmetic (.refl _)) (.eqSymm (.andL he))) (.arithmetic (.refl _)))
    (.eqMul (.arithmetic (.refl _)) (.eqSymm (.andR he))) baseDerivation

def stepContext : List Formula :=
  [oldGraphs (.succ (.var 0)) (.var 1) (.var 2), .lt (.var 2) valueBound,
    .lt (.var 1) valueBound, graphInvariant (.var 0), stepGraph, baseGraph]

def witnessContext : List Formula :=
  [stepWitness (.var 0), .lt (.var 7) (.lit 2),
    .exB 7 (.lit 2) (stepWitness (.var 0)), .lt (.var 6) valueBound,
    .exB 6 valueBound (.exB 7 (.lit 2) (stepWitness (.var 0))), .lt (.var 5) valueBound]
    ++ stepContext

def witnessInvariant : Derives witnessContext (invariant (.var 1) (.var 2)) := by
  have hw : Derives witnessContext (stepWitness (.var 0)) := hyp0
  have hi : Derives witnessContext (graphInvariant (.var 0)) :=
    push (push (push (push (push (push (push (push (push hyp0))))))))
  have hu : Derives witnessContext (.lt (.var 5) valueBound) :=
    push (push (push (push (push hyp0))))
  have hd : Derives witnessContext (.lt (.var 6) valueBound) :=
    push (push (push hyp0))
  have hp := Derives.impE
    (Derives.allBE 2 valueBound (.var 6) (by decide)
      (Derives.allBE 1 valueBound (.var 5) (by decide) hi hu) hd) (.andL hw)
  have hb := Derives.andR (Derives.andR (Derives.andR (Derives.andR hw)))
  have heu := Derives.andL (Derives.andR (Derives.andR hw))
  have hed := Derives.andL (Derives.andR (Derives.andR (Derives.andR hw)))
  exact .leRewrite
    (.eqAdd (.eqMul (.arithmetic (.refl _)) (.eqSymm heu)) (.arithmetic (.refl _)))
    (.eqMul (.arithmetic (.refl _)) (.eqSymm hed))
    (successorDerivation (.var 5) (.var 6) (.var 7) hp hb)

def stepInvariant : Derives traceContext
    (.allN 0 (.imp (graphInvariant (.var 0)) (graphInvariant (.succ (.var 0))))) := by
  apply Derives.allI 0 (by decide)
  apply Derives.impI
  apply Derives.allBI 1 valueBound (by decide) rfl
  apply Derives.allBI 2 valueBound (by decide) rfl
  apply Derives.impI
  have hs : Derives stepContext stepGraph := push (push (push (push hyp0)))
  have hu : Derives stepContext (.lt (.var 1) valueBound) := push (push hyp0)
  have hd : Derives stepContext (.lt (.var 2) valueBound) := push hyp0
  have he : Derives stepContext (stepExistentials (.var 0)) :=
    .impE (.allBE 2 valueBound (.var 2) (by decide)
      (.allBE 1 valueBound (.var 1) (by decide)
        (.allE 0 (.var 0) (by decide) hs) hu) hd) hyp0
  apply Derives.exBE 5 valueBound (by decide) (by decide) rfl he
  apply Derives.exBE 6 valueBound (by decide) (by decide) rfl hyp0
  apply Derives.exBE 7 (.lit 2) (by decide) (by decide) rfl hyp0
  exact witnessInvariant

/-- Actual use of IΣ₁ on a Δ₀ formula containing graph parameters. -/
def inductionFromTrace : Derives traceContext (.allN 0 (graphInvariant (.var 0))) :=
  .sigma1Induction 0 (.bounded rfl) (by decide) (by decide) (by decide)
    baseInvariant stepInvariant

/-- Closed conditional internal theorem; BaseGraph/StepGraph are discharged
implication antecedents, NEVER new theory axioms. -/
def graphInductionTheorem : Derives []
    (.imp baseGraph (.imp stepGraph (.allN 0 (graphInvariant (.var 0))))) :=
  .impI (.impI inductionFromTrace)

/-- EXACT guarded candidate from M04, not merely a semantic implication. -/
def guardedInvariant (k : Term) : Formula :=
  .imp (.le k stageBound) (graphInvariant k)

def guardedBase : Derives traceContext (guardedInvariant (.lit 0)) :=
  .impI (push baseInvariant)

def guardedStep : Derives traceContext
    (.allN 0 (.imp (guardedInvariant (.var 0)) (guardedInvariant (.succ (.var 0))))) := by
  apply Derives.allI 0 (by decide)
  apply Derives.impI
  apply Derives.impI
  have hk : Derives [.le (.succ (.var 0)) stageBound,
      guardedInvariant (.var 0), stepGraph, baseGraph] (.le (.var 0) stageBound) :=
    .leTrans (.ltLe (.ltSucc (.var 0))) hyp0
  have hi := Derives.impE (push hyp0) hk
  exact .impE (.allE 0 (.var 0) (by decide) (push (push stepInvariant))) hi

def guardedInduction : Derives traceContext (.allN 0 (guardedInvariant (.var 0))) :=
  .sigma1Induction 0 (.bounded rfl) (by decide) (by decide) (by decide)
    guardedBase guardedStep

def guardedGraphTheorem : Derives []
    (.imp baseGraph (.imp stepGraph (.allN 0 (guardedInvariant (.var 0))))) :=
  .impI (.impI guardedInduction)

/-- The bounded numerical trace relation to which code existence must apply.
T and the four β-code fields are free parameters, not assumed witnesses. -/
def traceValueRelations (k : Term) : Formula :=
  .conj (beta (.var 8) (.var 9) k (.var 5))
    (.conj (beta (.var 10) (.var 11) k (.var 6))
      (.conj (beta (.var 8) (.var 9) (.succ k) (.var 1))
        (beta (.var 10) (.var 11) (.succ k) (.var 2))))

def finiteTraceStep (k : Term) : Formula :=
  .exB 5 valueBound (.exB 6 valueBound (.exB 7 (.lit 2)
    (.exB 1 valueBound (.exB 2 valueBound
      (.conj (recurrenceValues k) (traceValueRelations k))))))

def finiteTraceMatrix : Formula :=
  .conj (.lt (.lit 1) valueBound)
    (.conj (beta (.var 8) (.var 9) (.lit 0) (.lit 0))
      (.conj (beta (.var 10) (.var 11) (.lit 0) (.lit 1))
        (.allB 0 stageBound (finiteTraceStep (.var 0)))))

theorem finiteTrace_is_bounded : finiteTraceMatrix.bounded = true := rfl
theorem invariant_is_bounded : (graphInvariant (.var 0)).bounded = true := rfl

#print axioms numeratorGraphExists
#print axioms denominatorGraphExists
#print axioms baseInvariant
#print axioms stepInvariant
#print axioms inductionFromTrace
#print axioms graphInductionTheorem
#print axioms finiteTrace_is_bounded
#print axioms guardedGraphTheorem

#eval ("graph_induction", ruleProfile graphInductionTheorem)
#eval ("M04_guarded_induction", ruleProfile guardedGraphTheorem)
#eval ("numerator_comprehension", ruleProfile numeratorGraphExists)
#eval ("denominator_comprehension", ruleProfile denominatorGraphExists)

end MatematicaAbierta.Continuo.TrazasInduccionRCA
