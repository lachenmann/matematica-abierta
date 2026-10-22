import MatematicaAbierta.Continuo.InvarianteCRTParcialRCA

/-! M11/T06. Uniform bounds depend only on N,b,P,C,R. Every new inverse
is obtained by multiplying explicit certificates, not a coprimality rule. -/
namespace MatematicaAbierta.Continuo.InversosFuturosRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA TrazasInduccionRCA
open DivisionInternaRCA DiferenciasInternasRCA AritmeticaModularInternaRCA
open InversosProductoRCA ProductoAcumuladoRCA InvarianteCRTParcialRCA

def J : Term := modulus N b
def H : Term := .add N (.lit 1)
def Q : Term := .mul (.mul H H) b
def L : Term := .add Q (.mul H b)
def B : Term := .succ (.add (.add (.lit 1) (.mul L J)) (.mul J Q))
def F : Term := .add (.mul C B) (productCoefficient C B J)
def U : Term := .add C (.mul p (.mul C (.add J R)))
def cap : Term := .succ (.add (.add (.lit 1) U) F)

def leOfLtSucc {Γ : List Formula} (t u : Term)
    (h : Proof Γ (.lt t (.succ u))) : Proof Γ (.le t u) := by
  apply Proof.orderCases t u
  · exact .ltLe hyp
  · exact .leRewrite (.eqSymm hyp) (eqRefl _) (leRefl u)
  · exact .botE (.ltIrrefl (.ltLeTrans (push h) (.ltSuccLe hyp)))

def modulusMono {Γ : List Formula} (i j param : Term)
    (h : Proof Γ (.le i j)) : Proof Γ (.le (modulus i param) (modulus j param)) :=
  leAddLeft (.lit 1) (.leMulRight param (.leAdd h (leRefl (.lit 1))))

def mulLe {Γ : List Formula} {a a' b b' : Term}
    (ha : Proof Γ (.le a a')) (hb : Proof Γ (.le b b')) :
    Proof Γ (.le (.mul a b) (.mul a' b')) :=
  .leTrans (.leMulRight b ha) (leMulLeft a' hb)

def coefficientLe {Γ : List Formula} {a a' b b' n n' : Term}
    (ha : Proof Γ (.le a a')) (hb : Proof Γ (.le b b'))
    (hn : Proof Γ (.le n n')) :
    Proof Γ (.le (productCoefficient a b n) (productCoefficient a' b' n')) :=
  .leAdd (.leAdd ha hb) (mulLe (mulLe ha hb) hn)

def capAboveU {Γ : List Formula} : Proof Γ (.lt U cap) :=
  leThenSucc (.leTrans (leLeftAdd U (.lit 1)) (leRightAdd (.add (.lit 1) U) F))
def capAboveF {Γ : List Formula} : Proof Γ (.lt F cap) :=
  leThenSucc (leLeftAdd F (.add (.lit 1) U))
def capAboveOne {Γ : List Formula} : Proof Γ (.lt (.lit 1) cap) :=
  leThenSucc (.leTrans (leRightAdd (.lit 1) U) (leRightAdd (.add (.lit 1) U) F))

def j : Term := .var 18
def pairResult : Formula := .exB 64 B (.exB 65 B
  (.conj (.lt (.lit 0) (.var 64))
    (.eq (.mul (.var 64) n) (.add (.lit 1) (.mul (.var 65) (modulus j b))))))
def pairΓ : List Formula := [.le j N,.lt k j,MultiploComunUniformeRCA.cm N b]
def gap : Formula := CompatibilidadProductoRCA.posGap.subst 3 N |>.subst 40 b |>.subst 20 k |>.subst 21 j
def gapProof : Proof pairΓ gap := by
  have h0 := Proof.allE 3 N (by decide) CompatibilidadProductoRCA.positiveDifferences
  have h1 := Proof.allE 40 b (by decide) h0
  have h2 := Proof.allE 20 k (by decide) h1
  have h3 := Proof.allE 21 j (by decide) h2
  exact .impE (.impE (.impE (SelectoresInternosRCA.closed h3)
    (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))) (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))) (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))

def δ : Term := .var 60
def c : Term := .var 61
def z : Term := .var 62
def hk : Term := .add k (.lit 1)
def hb : Term := .mul hk b
def qq : Term := .mul (.mul hk hk) c
def ll : Term := .add qq z
def gapΓ : List Formula := [
  .conj (.eq j (.add k δ)) (.conj (.lt (.lit 0) δ)
    (.exB 17 (.succ b) (.conj (.lt (.lit 0) (.var 17)) (.eq b (.mul δ (.var 17)))))),
  .lt δ (.succ N)] ++ pairΓ
def cΓ : List Formula := [.conj (.lt (.lit 0) c) (.eq b (.mul δ c)),.lt c (.succ b)] ++ gapΓ
def zΓ : List Formula := [.eq hb (.add (.lit 1) z),.lt z (.succ hb)] ++ cΓ

def predecessor : Proof cΓ (.exB 2 (.succ hb) (.eq hb (.add (.lit 1) (.var 2)))) := by
  have hc : Proof cΓ (.lt (.lit 0) c) := .andL (hyp : Proof cΓ _)
  have hd : Proof cΓ (.lt (.lit 0) δ) := .andL (.andR (push (push (hyp : Proof gapΓ _))))
  have he : Proof cΓ (.eq b (.mul δ c)) := .andR (hyp : Proof cΓ _)
  have bpos : Proof cΓ (.lt (.lit 0) b) :=
    .ltRewrite (eqRefl _) (.eqSymm he) (positiveProduct δ c hd hc)
  have hpos : Proof cΓ (.lt (.lit 0) hk) :=
    .ltRewrite (eqRefl _) (ax (.symm (addOne k))) (.leLtTrans (.zeroLe _) (ltSucc _))
  have oneLe : Proof cΓ (.le (.lit 1) hb) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _)
      (.ltSuccLe (positiveProduct hk b hpos bpos))
  exact .impE (.allBE 1 (.succ hb) (.lit 1) (by decide)
    (SelectoresInternosRCA.closed (.allE 0 hb (by decide) boundedDifference))
    (leThenSucc oneLe)) oneLe

def forward : Proof zΓ (.eq (.mul qq (modulus j b)) (.add (.lit 1) (.mul ll n))) :=
  IdentidadModulosBetaRCA.inverseEquality k j δ c b z
    (.andL (push (push (push (push (hyp : Proof gapΓ _))))))
    (.andR (push (push (hyp : Proof cΓ _))))
    (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))

def qLe : Proof zΓ (.le qq Q) := by
  have kj : Proof zΓ (.lt k j) := .hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)
  have jN : Proof zΓ (.le j N) := .hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)
  have hh := Proof.leAdd (.leTrans (.ltLe kj) jN) (leRefl (.lit 1))
  have cb : Proof zΓ (.le c b) := leOfLtSucc c b (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))
  exact mulLe (mulLe hh hh) cb
def lLe : Proof zΓ (.le ll L) := by
  have zz : Proof zΓ (.le z hb) :=
    .leRewrite (eqRefl _) (.eqSymm (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))) (leLeftAdd z (.lit 1))
  have kj : Proof zΓ (.lt k j) := .hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)
  have jN : Proof zΓ (.le j N) := .hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)
  exact .leAdd qLe (.leTrans zz (.leMulRight b (.leAdd (.leTrans (.ltLe kj) jN) (leRefl (.lit 1)))))
def nLe : Proof zΓ (.le n J) :=
  modulusMono k N b (.leTrans
    (.ltLe (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem) : Proof zΓ (.lt k j)))
    (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem) : Proof zΓ (.le j N)))
def reverse : Proof zΓ
    (swapConclusion.subst 20 n |>.subst 21 (modulus j b) |>.subst 22 qq |>.subst 23 ll) := by
  have h0 := Proof.allE 20 n (by decide) swapClosed
  have h1 := Proof.allE 21 (modulus j b) (by decide) h0
  have h2 := Proof.allE 22 qq (by decide) h1
  have h3 := Proof.allE 23 ll (by decide) h2
  exact .impE (.impE (SelectoresInternosRCA.closed h3) (modulusPositive _ _)) forward

def inverseΓ : List Formula := [
  .conj (.lt (.lit 0) (.var 64)) (.eq (.mul (.var 64) n)
    (.add (.lit 1) (.mul (.var 65) (modulus j b)))),
  .lt (.var 65) (.succ (.mul n qq)),
  .exB 33 (.succ (.mul n qq)) (.conj (.lt (.lit 0) (.var 64))
    (.eq (.mul (.var 64) n) (.add (.lit 1) (.mul (.var 33) (modulus j b))))),
  .lt (.var 64) (.succ (.add (.lit 1) (.mul ll n)))] ++ zΓ
def pairWitness : Proof inverseΓ pairResult := by
  have aBound : Proof inverseΓ (.lt (.var 64) B) :=
    .ltLeTrans (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)) (succLe (.leTrans
      (leAddLeft (.lit 1) (mulLe (push (push (push (push lLe)))) (push (push (push (push nLe))))))
      (leRightAdd (.add (.lit 1) (.mul L J)) (.mul J Q))))
  have vBound : Proof inverseΓ (.lt (.var 65) B) :=
    .ltLeTrans (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)) (succLe (.leTrans
      (mulLe (push (push (push (push nLe)))) (push (push (push (push qLe)))))
      (leLeftAdd (.mul J Q) (.add (.lit 1) (.mul L J)))))
  exact .exBI 64 B (.var 64) (by decide) aBound
    (.exBI 65 B (.var 65) (by decide) vBound (.hypothesis (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)))

def pairUniformOpen : Proof pairΓ pairResult := by
  apply Proof.exBErename 2 60 (.succ N) (by decide) (by decide) (by decide) (by decide) gapProof
  apply Proof.exBErename 17 61 (.succ b) (by decide) (by decide) (by decide) (by decide)
    (.andR (.andR (hyp : Proof gapΓ _)))
  apply Proof.exBErename 2 62 (.succ hb) (by decide) (by decide) (by decide) (by decide) predecessor
  apply Proof.exBErename 32 64 (.succ (.add (.lit 1) (.mul ll n)))
    (by decide) (by decide) (by decide) (by decide) reverse
  apply Proof.exBErename 33 65 (.succ (.mul n qq))
    (by decide) (by decide) (by decide) (by decide) hyp
  exact pairWitness
def pairUniform : Proof [] ([0,9,3,18].foldr Formula.allN
    (.imp (MultiploComunUniformeRCA.cm N b) (.imp (.lt k j) (.imp (.le j N) pairResult)))) :=
  .allI 0 rfl (.allI 9 rfl (.allI 3 rfl (.allI 18 rfl (.impI (.impI (.impI pairUniformOpen))))))

def futureΓ : List Formula := [future k p b N C,MultiploComunUniformeRCA.cm N b]
def pointΓ : List Formula := [.le (.succ k) j,.lt j (.succ N)] ++ futureΓ
def oldInverse : Formula := .exB 54 C (.exB 55 C
  (.conj (.lt (.lit 0) (.var 54))
    (.eq (.mul (.var 54) p) (.add (.lit 1) (.mul (.var 55) (modulus j b))))))
def newInverse : Formula := .exB 54 cap (.exB 55 cap
  (.conj (.lt (.lit 0) (.var 54))
    (.eq (.mul (.var 54) nextP) (.add (.lit 1) (.mul (.var 55) (modulus j b))))))
def oldAtJ : Proof pointΓ oldInverse := by
  have hj : Proof pointΓ (.lt j (.succ N)) := push hyp
  have hf : Proof pointΓ (future k p b N C) := push (push hyp)
  exact .impE (.allBE 18 (.succ N) j (by decide) hf hj)
    (.leTrans (leSucc k) hyp)
def pairAtJ : Proof pointΓ pairResult := by
  have h0 := Proof.allE 0 N (by decide) pairUniform
  have h1 := Proof.allE 9 b (by decide) h0
  have h2 := Proof.allE 3 k (by decide) h1
  have h3 := Proof.allE 18 j (by decide) h2
  exact .impE (.impE (.impE (SelectoresInternosRCA.closed h3)
    (push (push (push hyp)))) (.succLeLt hyp)) (leOfLtSucc j N (push hyp))
def u : Term := .var 66
def v : Term := .var 67
def storedΓ : List Formula := [
  .conj (.lt (.lit 0) u) (.eq (.mul u p) (.add (.lit 1) (.mul v (modulus j b)))),
  .lt v C,
  .exB 55 C (.conj (.lt (.lit 0) u)
    (.eq (.mul u p) (.add (.lit 1) (.mul (.var 55) (modulus j b))))),
  .lt u C] ++ pointΓ
def combinedΓ : List Formula := [
  .conj (.lt (.lit 0) (.var 64)) (.eq (.mul (.var 64) n)
    (.add (.lit 1) (.mul (.var 65) (modulus j b)))),
  .lt (.var 65) B,
  .exB 65 B (.conj (.lt (.lit 0) (.var 64))
    (.eq (.mul (.var 64) n) (.add (.lit 1) (.mul (.var 65) (modulus j b))))),
  .lt (.var 64) B] ++ storedΓ
def futureWitness : Proof combinedΓ newInverse := by
  have stored : Proof combinedΓ
      (.conj (.lt (.lit 0) u) (.eq (.mul u p) (.add (.lit 1) (.mul v (modulus j b))))) :=
    push (push (push (push (hyp : Proof storedΓ _))))
  have pair : Proof combinedΓ
      (.conj (.lt (.lit 0) (.var 64)) (.eq (.mul (.var 64) n)
        (.add (.lit 1) (.mul (.var 65) (modulus j b))))) := hyp
  have uC : Proof combinedΓ (.le u C) := .ltLe (.hypothesis
    (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))
  have vC : Proof combinedΓ (.le v C) := .ltLe (.hypothesis
    (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem))
  have aB : Proof combinedΓ (.le (.var 64) B) := .ltLe (push (push (push hyp)))
  have dB : Proof combinedΓ (.le (.var 65) B) := .ltLe (push hyp)
  have mjJ : Proof combinedΓ (.le (modulus j b) J) :=
    modulusMono j N b (leOfLtSucc j N (.hypothesis
      (by repeat first | exact List.mem_cons_self | apply List.mem_cons_of_mem)))
  apply Proof.exBI 54 cap (.mul u (.var 64)) (by decide)
    (.leLtTrans (.leTrans (mulLe uC aB) (leRightAdd (.mul C B) (productCoefficient C B J))) capAboveF)
  apply Proof.exBI 55 cap (productCoefficient v (.var 65) (modulus j b)) (by decide)
    (.leLtTrans (.leTrans (coefficientLe vC dB mjJ) (leLeftAdd (productCoefficient C B J) (.mul C B))) capAboveF)
  exact .andI (positiveProduct u (.var 64) (.andL stored) (.andL pair))
    (combineInverse p n (modulus j b) u (.var 64) v (.var 65) (.andR stored) (.andR pair))
def futurePoint : Proof pointΓ newInverse := by
  apply Proof.exBErename 54 66 C (by decide) (by decide) (by decide) (by decide) oldAtJ
  apply Proof.exBErename 55 67 C (by decide) (by decide) (by decide) (by decide) hyp
  apply Proof.exBErename 64 64 B (by decide) (by decide) (by decide) (by decide)
    (push (push (push (push pairAtJ))))
  apply Proof.exBErename 65 65 B (by decide) (by decide) (by decide) (by decide) hyp
  exact futureWitness
def futureStepOpen : Proof futureΓ (future (.succ k) nextP b N cap) := by
  apply Proof.allBI 18 (.succ N) (by decide) (by decide)
  apply Proof.impI
  exact futurePoint
def futureStep : Proof [] ([0,9,3,50,52,4].foldr Formula.allN
    (.imp (MultiploComunUniformeRCA.cm N b)
      (.imp (future k p b N C) (future (.succ k) nextP b N cap)))) :=
  .allI 0 rfl (.allI 9 rfl (.allI 3 rfl (.allI 50 rfl (.allI 52 rfl (.allI 4 rfl
    (.impI (.impI futureStepOpen)))))))

example : pairResult.bounded = true := by decide
example : pairResult.numFree.contains 60 = false := by decide
example : pairResult.numFree.contains 61 = false := by decide
example : pairResult.numFree.contains 62 = false := by decide
example : freshNum 64 zΓ = true := by decide
example : cap.vars.contains 60 = false := by decide
example : cap.vars.contains 61 = false := by decide
example : cap.vars.contains 62 = false := by decide
example : newInverse.bounded = true := by decide
example : newInverse.numFree.contains 64 = false := by decide
example : newInverse.numFree.contains 65 = false := by decide
example : newInverse.numFree.contains 66 = false := by decide
example : newInverse.numFree.contains 67 = false := by decide
example : freshNum 66 pointΓ = true := by decide
#print axioms leOfLtSucc
#print axioms modulusMono
#print axioms pairUniform
#print axioms futureStep
#eval ("uniform_special_pair_inverse", profile pairUniform)
#eval ("future_inverse_product_step_uniform_cap", profile futureStep)
end MatematicaAbierta.Continuo.InversosFuturosRCA
