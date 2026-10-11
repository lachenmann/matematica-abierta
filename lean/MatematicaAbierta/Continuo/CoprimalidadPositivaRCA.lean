import MatematicaAbierta.Continuo.CRTConstructivoDosRCA

/-! M08 C08. Coprimality is represented INTERNALLY by every positive common
divisor being 1. No gcd function or coprimality inference rule is introduced. -/
namespace MatematicaAbierta.Continuo.CoprimalidadPositivaRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA DiferenciasInternasRCA
open IdentidadModulosBetaRCA CRTConstructivoDosRCA

def oneAddPositive {Γ : List Formula} (t : Term) : Proof Γ (.lt t (.add (.lit 1) t)) :=
  .ltRewrite (ax (addZeroLeft t)) (eqRefl _)
    (.ltAddRight t (.embed ConstruccionBaseTrazaRCA.zeroLtOne))

def divisorOne {Γ : List Formula} (g t u : Term)
    (hg : Proof Γ (.lt (.lit 0) g))
    (he : Proof Γ (.eq (.mul g t) (.add (.lit 1) (.mul g u)))) :
    Proof Γ (.eq g (.lit 1)) := by
  have hOne : Proof Γ (.le (.lit 1) g) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe hg)
  apply Proof.orderCases g (.lit 1)
  · exact .botE (.ltIrrefl (.ltLeTrans hyp (push hOne)))
  · exact hyp
  · apply Proof.orderCases t u
    · have hgt : Proof (.lt t u :: .lt (.lit 1) g :: Γ) (.lt (.mul g u) (.mul g t)) :=
        .ltRewrite (eqRefl _) (.eqSymm (push (push he))) (oneAddPositive (.mul g u))
      have hle : Proof (.lt t u :: .lt (.lit 1) g :: Γ) (.le (.mul g t) (.mul g u)) :=
        .leRewrite (ax (.mulComm _ _)) (ax (.mulComm _ _)) (.leMulRight g (.ltLe hyp))
      exact .botE (.ltIrrefl (.ltLeTrans hgt hle))
    · have hgt : Proof (.eq t u :: .lt (.lit 1) g :: Γ) (.lt (.mul g u) (.mul g t)) :=
        .ltRewrite (eqRefl _) (.eqSymm (push (push he))) (oneAddPositive (.mul g u))
      exact .botE (.ltIrrefl (.ltRewrite (eqRefl _) (.eqMul (eqRefl g) hyp) hgt))
    · have hle : Proof (.lt u t :: .lt (.lit 1) g :: Γ)
          (.le (.add (.mul g u) g) (.mul g t)) :=
        .leRewrite (ax (.trans (CalculoOrdenRCA.mulSuccessorLeft u g)
          (.add (.mulComm _ _) (.refl _)))) (ax (.mulComm _ _))
            (.leMulRight g (.ltSuccLe hyp))
      have hlt : Proof (.lt u t :: .lt (.lit 1) g :: Γ)
          (.lt (.add (.mul g u) (.lit 1)) (.mul g t)) :=
        .ltLeTrans (ltAddLeft (.mul g u) (push hyp)) hle
      exact .botE (.ltIrrefl (.ltRewrite (ax (.addComm _ _)) (push (push he)) hlt))

def factorSwap (q g b : Term) : EqProof (.mul q (.mul g b)) (.mul g (.mul q b)) :=
  .trans (.symm (.mulAssoc _ _ _)) (swapFactors q g b)

def commonDivisorOne {Γ : List Formula} (q ell m n g a b : Term)
    (hi : Proof Γ (.eq (.mul q n) (.add (.lit 1) (.mul ell m))))
    (hm : Proof Γ (.eq m (.mul g a))) (hn : Proof Γ (.eq n (.mul g b)))
    (hg : Proof Γ (.lt (.lit 0) g)) : Proof Γ (.eq g (.lit 1)) := by
  have he : Proof Γ (.eq (.mul g (.mul q b)) (.add (.lit 1) (.mul g (.mul ell a)))) :=
    .eqTrans (.eqTrans (ax (.symm (factorSwap q g b))) (.eqSymm (.eqMul (eqRefl q) hn)))
      (.eqTrans hi (.eqAdd (eqRefl _)
        (.eqTrans (.eqMul (eqRefl ell) hm) (ax (factorSwap ell g a)))))
  exact divisorOne g (.mul q b) (.mul ell a) hg he

def specialContext : List Formula :=
  [.eq (modulus (.var 1) (.var 4)) (.mul (.var 26) (.var 28)),
   .eq (modulus (.var 0) (.var 4)) (.mul (.var 26) (.var 27)),
   .lt (.lit 0) (.var 26)] ++ identityContext

def inverseInContext : Proof specialContext conclusion := by
  have h0 := Proof.allE 0 (.var 0) (by decide) positiveInverse
  have h1 := Proof.allE 1 (.var 1) (by decide) h0
  have h2 := Proof.allE 2 (.var 2) (by decide) h1
  have h3 := Proof.allE 3 (.var 3) (by decide) h2
  have h4 := Proof.allE 4 (.var 4) (by decide) h3
  exact .impE (.impE (.impE (.impE (SelectoresInternosRCA.closed h4)
    (push (push (push (push (push (push hyp)))))))
    (push (push (push (push (push hyp))))))
    (push (push (push (push hyp))))) (push (push (push hyp)))

def specialOpen : Proof specialContext (.eq (.var 26) (.lit 1)) := by
  apply Proof.exBE 22 (.succ qCandidate) (by decide) (by decide) (by decide) inverseInContext
  apply Proof.exBE 23 (.succ (.add qCandidate hbTerm)) (by decide) (by decide) (by decide) hyp
  exact commonDivisorOne (.var 22) (.var 23) (modulus (.var 0) (.var 4)) (modulus (.var 1) (.var 4))
    (.var 26) (.var 27) (.var 28) (.andR hyp)
    (push (push (push (push (push hyp)))))
    (push (push (push (push hyp))))
    (push (push (push (push (push (push hyp))))))

def specialFormula : Formula := [0,1,2,3,4,26,27,28].foldr Formula.allN
  (.imp (.lt (.lit 0) (.var 3)) (.imp (.lt (.lit 0) (.var 2))
    (.imp (.eq (.var 4) (.mul (.var 2) (.var 3)))
      (.imp (.eq (.var 1) (.add (.var 0) (.var 2)))
        (.imp (.lt (.lit 0) (.var 26))
          (.imp (.eq (modulus (.var 0) (.var 4)) (.mul (.var 26) (.var 27)))
            (.imp (.eq (modulus (.var 1) (.var 4)) (.mul (.var 26) (.var 28)))
              (.eq (.var 26) (.lit 1)))))))))
def specialCoprime : Proof [] specialFormula := by
  apply Proof.allI 0 rfl
  apply Proof.allI 1 rfl
  apply Proof.allI 2 rfl
  apply Proof.allI 3 rfl
  apply Proof.allI 4 rfl
  apply Proof.allI 26 rfl
  apply Proof.allI 27 rfl
  apply Proof.allI 28 rfl
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  apply Proof.impI
  exact specialOpen

example : specialFormula.numFree = [] := by decide
example : specialFormula.setFree = [] := by decide
#print axioms divisorOne
#print axioms commonDivisorOne
#print axioms specialCoprime
#eval ("special_moduli_common_divisor_one", profile specialCoprime)
end MatematicaAbierta.Continuo.CoprimalidadPositivaRCA
