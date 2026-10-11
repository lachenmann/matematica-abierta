import MatematicaAbierta.Continuo.LecturasBetaRCA
import MatematicaAbierta.Continuo.EmparejamientoInternoRCA

/-! H04-04.f/g: rename the M05 selectors internally before reading at
P(k,u). Their original bound names 1,2 would capture actual values 1,2.
The fresh selectors use 16,17. No alpha-equivalence axiom is introduced:
both directions below are built with existential introduction/elimination.
-/
namespace MatematicaAbierta.Continuo.SelectoresInternosRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA EmparejamientoInternoRCA

inductive Channel where | u | d deriving DecidableEq, Repr
def graphSet : Channel → ℕ | .u => 0 | .d => 1
def codeA : Channel → Term | .u => .var 8 | .d => .var 10
def codeB : Channel → Term | .u => .var 9 | .d => .var 11
def originalMatrix (c : Channel) : Formula := graphMatrix (codeA c) (codeB c)
def originalSpec (c : Channel) : Formula :=
  .allN 0 (iffF (.member (.var 0) (graphSet c)) (originalMatrix c))
def namedBody (c : Channel) : Formula :=
  .conj (.eq (.var 0) (pair (.var 16) (.var 17)))
    (.conj (.le (.var 16) stageBound)
      (.conj (.lt (.var 17) valueBound) (beta (codeA c) (codeB c) (.var 16) (.var 17))))
def namedMatrix (c : Channel) : Formula :=
  .exB 16 (.succ (.var 0)) (.exB 17 (.succ (.var 0)) (namedBody c))
def namedSpec (c : Channel) : Formula :=
  .allN 0 (iffF (.member (.var 0) (graphSet c)) (namedMatrix c))

def closed {Γ : List Formula} {p : Formula} (h : Proof [] p) : Proof Γ p :=
  .weaken (fun _ hm => False.elim (List.not_mem_nil hm)) h

def alphaForward (c : Channel) : Proof [originalMatrix c] (namedMatrix c) := by
  apply Proof.exBErename 1 16 (.succ (.var 0))
    (by cases c <;> decide) (by cases c <;> decide) rfl (by cases c <;> decide) hyp
  apply Proof.exBErename 2 17 (.succ (.var 0))
    (by cases c <;> decide) (by cases c <;> decide) rfl (by cases c <;> decide) hyp
  apply Proof.exBI 16 (.succ (.var 0)) (.var 16) (by cases c <;> decide)
  · exact push (push (push hyp))
  apply Proof.exBI 17 (.succ (.var 0)) (.var 17) (by cases c <;> decide)
  · exact push hyp
  cases c <;> exact hyp

def alphaBackward (c : Channel) : Proof [namedMatrix c] (originalMatrix c) := by
  apply Proof.exBE 16 (.succ (.var 0))
    (by cases c <;> decide) (by cases c <;> decide) rfl hyp
  apply Proof.exBE 17 (.succ (.var 0))
    (by cases c <;> decide) (by cases c <;> decide) rfl hyp
  apply Proof.exBI 1 (.succ (.var 0)) (.var 16) (by cases c <;> decide)
  · exact push (push (push hyp))
  apply Proof.exBI 2 (.succ (.var 0)) (.var 17) (by cases c <;> decide)
  · exact push hyp
  cases c <;> exact hyp

def alphaSelectors (c : Channel) : Proof []
    (.allN 0 (iffF (originalMatrix c) (namedMatrix c))) :=
  .allI 0 rfl (.andI (.impI (alphaForward c)) (.impI (alphaBackward c)))

def renameSpecification (c : Channel) : Proof [] (.imp (originalSpec c) (namedSpec c)) := by
  apply Proof.impI
  apply Proof.allI 0 (by cases c <;> decide)
  apply Proof.andI
  · apply Proof.impI
    have he : Proof [.member (.var 0) (graphSet c),originalSpec c]
        (iffF (originalMatrix c) (namedMatrix c)) := by
      let h := alphaSelectors c
      cases c <;> exact Proof.allE 0 (.var 0) (by decide) (closed h)
    have hs : Proof [.member (.var 0) (graphSet c),originalSpec c]
        (iffF (.member (.var 0) (graphSet c)) (originalMatrix c)) := by
      have ho : Proof [.member (.var 0) (graphSet c),originalSpec c] (originalSpec c) := push hyp
      cases c <;> exact Proof.allE 0 (.var 0) (by decide) ho
    exact .impE (.andL he) (.impE (.andL hs) hyp)
  · apply Proof.impI
    have he : Proof [namedMatrix c,originalSpec c] (iffF (originalMatrix c) (namedMatrix c)) := by
      let h := alphaSelectors c
      cases c <;> exact Proof.allE 0 (.var 0) (by decide) (closed h)
    have hs : Proof [namedMatrix c,originalSpec c]
        (iffF (.member (.var 0) (graphSet c)) (originalMatrix c)) := by
      have ho : Proof [namedMatrix c,originalSpec c] (originalSpec c) := push hyp
      cases c <;> exact Proof.allE 0 (.var 0) (by decide) ho
    exact .impE (.andR hs) (.impE (.andR he) hyp)

inductive Stage where | zero | current | successor deriving DecidableEq, Repr
def stageTerm : Stage → Term | .zero => .lit 0 | .current => .var 0 | .successor => .succ (.var 0)
inductive Value where | u | d | oldU | oldD deriving DecidableEq, Repr
def valueTerm : Value → Term | .u => .var 1 | .d => .var 2 | .oldU => .var 5 | .oldD => .var 6
def reading (c : Channel) (s : Stage) (v : Value) : Formula :=
  .conj (.le (stageTerm s) stageBound)
    (.conj (.lt (valueTerm v) valueBound) (beta (codeA c) (codeB c) (stageTerm s) (valueTerm v)))
def memberAt (c : Channel) (s : Stage) (v : Value) : Formula :=
  .member (pair (stageTerm s) (valueTerm v)) (graphSet c)
def decodeContext (c : Channel) (s : Stage) (v : Value) : List Formula :=
  [memberAt c s v,namedSpec c]
def decodedWitness (c : Channel) (s : Stage) (v : Value) : Formula :=
  (namedBody c).subst 0 (pair (stageTerm s) (valueTerm v))
def decodeWitnessContext (c : Channel) (s : Stage) (v : Value) : List Formula :=
  [decodedWitness c s v,.lt (.var 17) (.succ (pair (stageTerm s) (valueTerm v))),
   .exB 17 (.succ (pair (stageTerm s) (valueTerm v))) (decodedWitness c s v),
   .lt (.var 16) (.succ (pair (stageTerm s) (valueTerm v)))] ++ decodeContext c s v

def decodeWitness (c : Channel) (s : Stage) (v : Value) :
    Proof (decodeWitnessContext c s v) (reading c s v) := by
  have hw : Proof (decodeWitnessContext c s v) (decodedWitness c s v) := hyp
  have hp : Proof (decodeWitnessContext c s v)
      (.eq (pair (stageTerm s) (valueTerm v)) (pair (.var 16) (.var 17))) := by
    cases c <;> cases s <;> cases v <;> exact Proof.andL hw
  have hi := pairInjectiveOpen (stageTerm s) (valueTerm v) (.var 16) (.var 17) hp
  have hk := Proof.andL hi
  have hv := Proof.andR hi
  have hstage : Proof (decodeWitnessContext c s v) (.le (.var 16) stageBound) := by
    cases c <;> cases s <;> cases v <;> exact Proof.andL (Proof.andR hw)
  have hvalue : Proof (decodeWitnessContext c s v) (.lt (.var 17) valueBound) := by
    cases c <;> cases s <;> cases v <;> exact Proof.andL (Proof.andR (Proof.andR hw))
  have hb : Proof (decodeWitnessContext c s v) (beta (codeA c) (codeB c) (.var 16) (.var 17)) := by
    cases c <;> cases s <;> cases v <;> exact Proof.andR (Proof.andR (Proof.andR hw))
  have hbk : Proof (decodeWitnessContext c s v)
      (beta (codeA c) (codeB c) (stageTerm s) (.var 17)) := by
    let a := codeA c
    let b := codeB c
    let k := stageTerm s
    cases c <;> cases s <;> cases v <;>
      exact Proof.eqSubst (beta a b (.var 20) (.var 17)) 20
        (.var 16) k (by decide) (by decide) (Proof.eqSymm hk) hb
  have hbu : Proof (decodeWitnessContext c s v)
      (beta (codeA c) (codeB c) (stageTerm s) (valueTerm v)) := by
    let a := codeA c
    let b := codeB c
    let k := stageTerm s
    let u := valueTerm v
    cases c <;> cases s <;> cases v <;>
      exact Proof.eqSubst (beta a b k (.var 21)) 21
        (.var 17) u (by decide) (by decide) (Proof.eqSymm hv) hbk
  exact .andI (.leRewrite (.eqSymm hk) (eqRefl _) hstage)
    (.andI (.ltRewrite (.eqSymm hv) (eqRefl _) hvalue) hbu)

def decodeGraph (c : Channel) (s : Stage) (v : Value) : Proof []
    (.imp (namedSpec c) (.imp (memberAt c s v) (reading c s v))) := by
  apply Proof.impI
  apply Proof.impI
  have hspec : Proof (decodeContext c s v)
      (iffF (memberAt c s v) ((namedMatrix c).subst 0 (pair (stageTerm s) (valueTerm v)))) :=
    .allE 0 (pair (stageTerm s) (valueTerm v)) (by cases c <;> cases s <;> cases v <;> decide) (push hyp)
  have hm := Proof.impE (Proof.andL hspec) hyp
  apply Proof.exBE 16 (.succ (pair (stageTerm s) (valueTerm v)))
    (by cases c <;> cases s <;> cases v <;> decide)
    (by cases c <;> cases s <;> cases v <;> decide)
    (by cases s <;> cases v <;> decide) hm
  apply Proof.exBE 17 (.succ (pair (stageTerm s) (valueTerm v)))
    (by cases c <;> cases s <;> cases v <;> decide)
    (by cases c <;> cases s <;> cases v <;> decide)
    (by cases s <;> cases v <;> decide) hyp
  exact decodeWitness c s v

def encodeGraph (c : Channel) (s : Stage) (v : Value) : Proof []
    (.imp (namedSpec c) (.imp (reading c s v) (memberAt c s v))) := by
  apply Proof.impI
  apply Proof.impI
  have hs : Proof [reading c s v,namedSpec c]
      (iffF (memberAt c s v) ((namedMatrix c).subst 0 (pair (stageTerm s) (valueTerm v)))) :=
    .allE 0 (pair (stageTerm s) (valueTerm v)) (by cases c <;> cases s <;> cases v <;> decide) (push hyp)
  apply Proof.impE (Proof.andR hs)
  apply Proof.exBI 16 (.succ (pair (stageTerm s) (valueTerm v))) (stageTerm s)
    (by cases c <;> cases s <;> cases v <;> decide) (firstProjectionBound (stageTerm s) (valueTerm v))
  let k := stageTerm s
  let u := valueTerm v
  cases s <;> cases v <;>
    apply Proof.exBI 17 (.succ (pair k u)) u
      (by cases c <;> decide) (secondProjectionBound k u)
  all_goals cases c <;> exact Proof.andI (eqRefl _) hyp

def betaFreshBody : Formula :=
  .imp (beta (.var 8) (.var 9) (.var 0) (.var 18))
    (.imp (beta (.var 8) (.var 9) (.var 0) (.var 19)) (.eq (.var 18) (.var 19)))
def betaUniqueFresh : Proof []
    (.allN 8 (.allN 9 (.allN 0 (.allN 18 (.allN 19 betaFreshBody))))) := by
  apply Proof.allI 8 rfl
  apply Proof.allI 9 rfl
  apply Proof.allI 0 rfl
  apply Proof.allI 18 rfl
  apply Proof.allI 19 rfl
  exact Proof.allE 2 (.var 19) (by decide)
    (Proof.allE 1 (.var 18) (by decide)
      (Proof.allE 0 (.var 0) (by decide)
        (Proof.allE 9 (.var 9) (by decide)
          (Proof.allE 8 (.var 8) (by decide) LecturasBetaRCA.betaUnique))))

inductive ComparedValue where | zero | one | traceU | traceD deriving DecidableEq, Repr
def comparedTerm : ComparedValue → Term
  | .zero => .lit 0 | .one => .lit 1 | .traceU => .var 18 | .traceD => .var 19
def betaSpecialized (c : Channel) (s : Stage) (v : Value) (w : ComparedValue) : Proof []
    (.imp (beta (codeA c) (codeB c) (stageTerm s) (valueTerm v))
      (.imp (beta (codeA c) (codeB c) (stageTerm s) (comparedTerm w))
        (.eq (valueTerm v) (comparedTerm w)))) := by
  let a := codeA c
  let b := codeB c
  let k := stageTerm s
  let u := valueTerm v
  let t := comparedTerm w
  cases c <;> cases s <;> cases v <;> cases w <;>
    exact Proof.allE 19 t (by decide)
      (Proof.allE 18 u (by decide)
        (Proof.allE 0 k (by decide)
          (Proof.allE 9 b (by decide)
            (Proof.allE 8 a (by decide) betaUniqueFresh))))

#print axioms alphaSelectors
#print axioms renameSpecification
#print axioms decodeGraph
#print axioms encodeGraph
#print axioms betaSpecialized
#eval ("selector_decode_U", profile (decodeGraph .u .current .u))
#eval ("selector_encode_U", profile (encodeGraph .u .current .oldU))
end MatematicaAbierta.Continuo.SelectoresInternosRCA
