import MatematicaAbierta.Continuo.SelectoresInternosRCA

/-! H04-04.d: an actual Delta₁ graph-append construction. Its selector
is ¬(x=P(K+1,v_new)) → x∈G_old. Both preservation on k≤K and the appended
slot are internally derived. This is SET-coded append, NOT uniform numeric
beta-code extension/CRT; that numeric obligation remains open.
-/
namespace MatematicaAbierta.Continuo.ExtensionGraficaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA SelectoresInternosRCA EmparejamientoInternoRCA

def newSet : Channel → ℕ | .u => 3 | .d => 4
def newValue : Channel → Term | .u => .var 18 | .d => .var 19
def appendPair (c : Channel) : Term := pair (.succ stageBound) (newValue c)
def appendMatrix (c : Channel) : Formula :=
  .imp (.imp (.eq (.var 0) (appendPair c)) .bot) (.member (.var 0) (graphSet c))
def appendSpec (c : Channel) : Formula :=
  .allN 0 (iffF (.member (.var 0) (newSet c)) (appendMatrix c))

def appendGraphExists (c : Channel) : Proof [] (.exS (newSet c) (appendSpec c)) :=
  .embed (.delta1Comprehension 0 (newSet c) (.bounded rfl) (.bounded rfl) rfl
    (by cases c <;> decide) (by cases c <;> decide)
    (.allI 0 rfl (.andI (.impI TrazasInduccionRCA.hyp0) (.impI TrazasInduccionRCA.hyp0))))

def distinctSlot {Γ : List Formula} (k u K v : Term) (hk : Proof Γ (.le k K)) :
    Proof Γ (.imp (.eq (pair k u) (pair (.succ K) v)) .bot) := by
  apply Proof.impI
  have hi : Proof (.eq (pair k u) (pair (.succ K) v) :: Γ)
      (.conj (.eq k (.succ K)) (.eq u v)) := pairInjectiveOpen k u (.succ K) v hyp
  exact .ltIrrefl (.succLeLt (.leRewrite (.andL hi) (eqRefl K) (push hk)))

def preservation (c : Channel) : Proof []
    (.imp (appendSpec c) (.allN 0 (.allN 1
      (.imp (.le (.var 0) stageBound)
        (iffF (.member (pair (.var 0) (.var 1)) (newSet c))
          (.member (pair (.var 0) (.var 1)) (graphSet c))))))) := by
  apply Proof.impI
  apply Proof.allI 0 (by cases c <;> decide)
  apply Proof.allI 1 (by cases c <;> decide)
  apply Proof.impI
  apply Proof.andI
  · apply Proof.impI
    have hsp : Proof [.member (pair (.var 0) (.var 1)) (newSet c),
        .le (.var 0) stageBound,appendSpec c] (appendSpec c) := push (push hyp)
    have hs : Proof [.member (pair (.var 0) (.var 1)) (newSet c),
        .le (.var 0) stageBound,appendSpec c]
        (iffF (.member (pair (.var 0) (.var 1)) (newSet c))
          (.imp (.imp (.eq (pair (.var 0) (.var 1)) (appendPair c)) .bot)
            (.member (pair (.var 0) (.var 1)) (graphSet c)))) := by
      let h := hsp
      cases c <;> exact Proof.allE 0 (pair (.var 0) (.var 1)) (by decide) h
    exact .impE (.impE (.andL hs) hyp)
      (distinctSlot (.var 0) (.var 1) stageBound (newValue c) (push hyp))
  · apply Proof.impI
    have hsp : Proof [.member (pair (.var 0) (.var 1)) (graphSet c),
        .le (.var 0) stageBound,appendSpec c] (appendSpec c) := push (push hyp)
    have hs : Proof [.member (pair (.var 0) (.var 1)) (graphSet c),
        .le (.var 0) stageBound,appendSpec c]
        (iffF (.member (pair (.var 0) (.var 1)) (newSet c))
          (.imp (.imp (.eq (pair (.var 0) (.var 1)) (appendPair c)) .bot)
            (.member (pair (.var 0) (.var 1)) (graphSet c)))) := by
      let h := hsp
      cases c <;> exact Proof.allE 0 (pair (.var 0) (.var 1)) (by decide) h
    exact .impE (.andR hs) (.impI (push hyp))

def appendLast (c : Channel) : Proof []
    (.imp (appendSpec c) (.member (appendPair c) (newSet c))) := by
  apply Proof.impI
  have hs : Proof [appendSpec c]
      (iffF (.member (appendPair c) (newSet c))
        (.imp (.imp (.eq (appendPair c) (appendPair c)) .bot)
          (.member (appendPair c) (graphSet c)))) := by
    have hsp : Proof [appendSpec c] (appendSpec c) := hyp
    cases c <;> exact Proof.allE 0 (appendPair _) (by decide) hsp
  exact .impE (.andR hs) (.impI (.botE (.impE hyp (eqRefl (appendPair c)))))

#print axioms appendGraphExists
#print axioms preservation
#print axioms appendLast
#eval ("graph_append_comprehension", profile (appendGraphExists .u))
#eval ("graph_append_preservation", profile (preservation .u))
end MatematicaAbierta.Continuo.ExtensionGraficaRCA
