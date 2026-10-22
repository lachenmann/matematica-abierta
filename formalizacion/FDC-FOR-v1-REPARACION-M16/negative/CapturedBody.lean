import MatematicaAbierta.Continuo.RechazoContraejemploM15RCA
open MatematicaAbierta.Continuo CalculoRCA CalculoOrdenRCA RechazoContraejemploM15RCA
def capturedCounterexample : Proof [] .bot :=
  .exBErename 170 171 (.lit 2) rfl rfl rfl rfl (by decide) (by decide)
    existsDifferentProof renamedBranch
