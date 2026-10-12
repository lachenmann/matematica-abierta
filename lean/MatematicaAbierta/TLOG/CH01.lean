import Lean

/- Experimental CPL syntax. No claim of unique readability or approved certification. -/
namespace MatematicaAbierta.TLOG.CH01

abbrev PV := { n : Nat // 1 ≤ n }

inductive BinOp where
  | conj
  | disj
  | imp
  | bicond
  deriving DecidableEq, Repr

inductive Token where
  | atom (v : PV)
  | negSymbol
  | binarySymbol (op : BinOp)
  | leftParen
  | rightParen
  deriving DecidableEq, Repr

abbrev Expression := List Token

def Eneg (s : Expression) : Expression :=
  [Token.leftParen, Token.negSymbol] ++ s ++ [Token.rightParen]

def Ebin (b : BinOp) (s t : Expression) : Expression :=
  [Token.leftParen] ++ s ++ [Token.binarySymbol b] ++ t ++ [Token.rightParen]

inductive Formula where
  | atom (v : PV)
  | neg (a : Formula)
  | binary (b : BinOp) (a c : Formula)
  deriving DecidableEq, Repr

def render : Formula → Expression
  | .atom v => [Token.atom v]
  | .neg a => Eneg (render a)
  | .binary b a c => Ebin b (render a) (render c)

inductive Wff : Expression → Prop where
  | atom (v : PV) : Wff [Token.atom v]
  | neg {s : Expression} : Wff s → Wff (Eneg s)
  | binary (b : BinOp) {s t : Expression} : Wff s → Wff t → Wff (Ebin b s t)

theorem abstract_structural_induction (P : Formula → Prop)
    (hatom : ∀ v : PV, P (.atom v))
    (hneg : ∀ a : Formula, P a → P (.neg a))
    (hbin : ∀ b : BinOp, ∀ a c : Formula, P a → P c → P (.binary b a c))
    (f : Formula) : P f := by
  induction f with
  | atom v => exact hatom v
  | neg a ih => exact hneg a ih
  | binary b a c iha ihc => exact hbin b a c iha ihc

theorem render_wff (f : Formula) : Wff (render f) := by
  induction f with
  | atom v => exact Wff.atom v
  | neg a ih => exact Wff.neg ih
  | binary b a c iha ihc => exact Wff.binary b iha ihc

theorem wff_iff_render (s : Expression) : Wff s ↔ ∃ f : Formula, render f = s := by
  constructor
  · intro h
    induction h with
    | atom v => exact ⟨.atom v, rfl⟩
    | @neg s hs ih =>
      obtain ⟨f, hf⟩ := ih
      exact ⟨.neg f, congrArg Eneg hf⟩
    | @binary b s t hs ht ihs iht =>
      obtain ⟨a, ha⟩ := ihs
      obtain ⟨c, hc⟩ := iht
      exact ⟨.binary b a c, by simp only [render, ha, hc]⟩
  · intro h
    obtain ⟨f, hf⟩ := h
    exact hf ▸ render_wff f

theorem concrete_structural_induction (P : Expression → Prop)
    (hatom : ∀ v : PV, P [Token.atom v])
    (hneg : ∀ s : Expression, Wff s → P s → P (Eneg s))
    (hbin : ∀ b : BinOp, ∀ s t : Expression,
      Wff s → Wff t → P s → P t → P (Ebin b s t))
    (s : Expression) (h : Wff s) : P s := by
  induction h with
  | atom v => exact hatom v
  | @neg s hs ih => exact hneg s hs ih
  | @binary b s t hs ht ihs iht => exact hbin b s t hs ht ihs iht

def Closed (S : Expression → Prop) : Prop :=
  (∀ v : PV, S [Token.atom v]) ∧
  (∀ s : Expression, S s → S (Eneg s)) ∧
  (∀ b : BinOp, ∀ s t : Expression, S s → S t → S (Ebin b s t))

theorem wff_closed : Closed Wff :=
  ⟨Wff.atom, fun _ h => Wff.neg h, fun b _ _ hs ht => Wff.binary b hs ht⟩

theorem wff_least (S : Expression → Prop) (closed : Closed S)
    (s : Expression) (hs : Wff s) : S s :=
  concrete_structural_induction S closed.1
    (fun a _ ha => closed.2.1 a ha)
    (fun b a c _ _ ha hc => closed.2.2 b a c ha hc) s hs

theorem wff_iff_all_closed (s : Expression) :
    Wff s ↔ ∀ S : Expression → Prop, Closed S → S s := by
  constructor
  · intro hs S closed
    exact wff_least S closed s hs
  · intro h
    exact h Wff wff_closed

abbrev Fm := { s : Expression // Wff s }

namespace Fm
def atom (v : PV) : Fm := ⟨[Token.atom v], Wff.atom v⟩
def neg (a : Fm) : Fm := ⟨Eneg a.val, Wff.neg a.property⟩
def binary (b : BinOp) (a c : Fm) : Fm :=
  ⟨Ebin b a.val c.val, Wff.binary b a.property c.property⟩
end Fm

/- TLOG-MTH-00001: P ranges over the concrete well-formed written expressions. -/
theorem tlog_mth_00001 (P : Fm → Prop)
    (hatom : ∀ v : PV, P (Fm.atom v))
    (hneg : ∀ a : Fm, P a → P (Fm.neg a))
    (hbin : ∀ b : BinOp, ∀ a c : Fm, P a → P c → P (Fm.binary b a c))
    (φ : Fm) : P φ := by
  obtain ⟨s, hs⟩ := φ
  induction hs with
  | atom v => exact hatom v
  | @neg s hs ih => exact hneg ⟨s, hs⟩ ih
  | @binary b s t hs ht ihs iht => exact hbin b ⟨s, hs⟩ ⟨t, ht⟩ ihs iht

end MatematicaAbierta.TLOG.CH01
