import Lean

/-! M16 elaboration-only inventory. It adds no proof rule or axiom. -/
open Lean Elab Tactic Meta
elab "audit_rename " label:str " using " rule:term : tactic => do
  let goal ← getMainGoal
  evalTactic (← `(tactic| apply $rule))
  let e ← instantiateMVars (mkMVar goal)
  let args := e.consumeMData.getAppArgs
  unless args.size ≥ 6 do throwError "Expected a specialized existential elimination"
  let p ← reduce args[1]!
  let context ← reduce args[0]!
  let conclusion ← reduce args[2]!
  let identity := e.consumeMData.getAppFn.isConstOf `MatematicaAbierta.Continuo.CalculoOrdenRCA.Proof.exBE
  let y := if identity then args[3]! else args[4]!
  let bound ← reduce args[if identity then 4 else 5]!
  logInfo m!"M16_AUDIT {label.getString}\nx={args[3]!}; y={y}; identity={identity}\np={p}\ncontext={context}\nconclusion={conclusion}\nbound={bound}"
