import MatematicaAbierta.Continuo.CalculoRCA
import MatematicaAbierta.Continuo.CertificadosOrdenFinito
import Mathlib.Tactic

/-!
H04-05: translate the CONCRETE M04 certificate, including both hypothesis
leaves and conclusion. The target is a deep arithmetic derivation, not a proof
of a Nat inequality. Reification equalities/provenance use the old polynomial
container; the actual derivation and its universal closure do not.
No generic extraction from arbitrary quotient-polynomial transports is claimed.
-/
namespace MatematicaAbierta.Continuo.PuenteCertificadoRCA
open CalculoRCA
namespace Source
open CertificadosOrdenFinito
noncomputable abbrev Context := successorContext
noncomputable abbrev Left := (3 * (4 * u + 2 * b) + 2 : Poly)
noncomputable abbrev Right := (2 * (4 * d) : Poly)
end Source

noncomputable def polynomial : Term → CertificadosOrdenFinito.Poly
  | .lit n => MvPolynomial.C n
  | .var n => MvPolynomial.X n
  | .succ t => polynomial t + 1
  | .add t u => polynomial t + polynomial u
  | .mul t u => polynomial t * polynomial u

noncomputable def inequalityImage : Formula → Option
    (CertificadosOrdenFinito.Poly × CertificadosOrdenFinito.Poly)
  | .le t u => some (polynomial t, polynomial u)
  | _ => none

def deepContext : List Formula :=
  [invariant (.var 0) (.var 1), .le (.var 2) (.lit 1)]

def deepConclusion : Formula :=
  invariant (.add (.mul (.lit 4) (.var 0)) (.mul (.lit 2) (.var 2)))
    (.mul (.lit 4) (.var 1))

def successorClosed : Derives deepContext deepConclusion :=
  successorDerivation (.var 0) (.var 1) (.var 2)
    (.hypothesis List.mem_cons_self)
    (.hypothesis (List.mem_cons_of_mem _ List.mem_cons_self))

def successorUniversal : Derives []
    (.allN 0 (.allN 1 (.allN 2
      (.imp (invariant (.var 0) (.var 1)) (.imp (.le (.var 2) (.lit 1)) deepConclusion))))) :=
  .allI 0 rfl (.allI 1 rfl (.allI 2 rfl
    (.impI (.impI (successorDerivation (.var 0) (.var 1) (.var 2)
      (.hypothesis (List.mem_cons_of_mem _ List.mem_cons_self))
      (.hypothesis List.mem_cons_self))))))

theorem context_image : deepContext.map inequalityImage = Source.Context.map some := by
  norm_num [deepContext, inequalityImage, invariant, polynomial, Source.Context,
    CertificadosOrdenFinito.successorContext, CertificadosOrdenFinito.u,
    CertificadosOrdenFinito.d, CertificadosOrdenFinito.b]

theorem conclusion_image : inequalityImage deepConclusion = some (Source.Left, Source.Right) := by
  norm_num [inequalityImage, deepConclusion, invariant, polynomial, Source.Left,
    Source.Right, CertificadosOrdenFinito.u, CertificadosOrdenFinito.d, CertificadosOrdenFinito.b]

/-- Concrete, fully checked provenance and syntactic target certificate. -/
structure Translation where
  source : CertificadosOrdenFinito.Certificate Source.Context Source.Left Source.Right
  target : Derives deepContext deepConclusion
  hypotheses_match : deepContext.map inequalityImage = Source.Context.map some
  conclusion_matches : inequalityImage deepConclusion = some (Source.Left, Source.Right)

noncomputable def translation : Translation :=
  ⟨CertificadosOrdenFinito.successorCertificate, successorClosed, context_image, conclusion_image⟩

#print axioms successorClosed
#print axioms successorUniversal
#print axioms context_image
#print axioms conclusion_image
#print axioms translation

#eval ("successor_universal", ruleProfile successorUniversal)

end MatematicaAbierta.Continuo.PuenteCertificadoRCA
