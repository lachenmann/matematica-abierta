import unittest

from adapters.mcl import forbidden_tactics, parse_axioms, validate_mapping, validate_profile
from adapters.mcl_runner import find_exercise, policy_check, render_submission, tactic_heads


class TestMCLAdapter(unittest.TestCase):
    def test_profile(self):
        profile = {
            "schema_version": "1",
            "profile_id": "mcl",
            "project": "MatematicaAbierta",
            "lean_root": "lean",
            "library": "MatematicaAbierta",
            "module_root": "MatematicaAbierta.MCL",
            "toolchain_file": "lean/lean-toolchain",
            "manifest": "lean/lake-manifest.json",
            "workflow": ".github/workflows/lean.yml",
            "source_kind": "mcl-human",
            "source_id_pattern": "^MCL-"
        }
        self.assertEqual(validate_profile(profile), [])

    def test_mapping_ids_and_roles(self):
        mapping = {
            "lesson_id": "MCL-U00-L01",
            "entries": [{
                "id": "MCL-U00-L01-E01",
                "role": "example",
                "declaration": "MatematicaAbierta.MCL.U00.L01.dos_es_dos"
            }],
            "productive_errors": [{
                "id": "MCL-U00-L01-X01",
                "role": "productive-error",
                "expected_kernel_result": "reject",
                "code": "example : (2 : Nat) = 3 := by rfl"
            }]
        }
        self.assertEqual(validate_mapping(mapping), [])

    def test_forbidden_tactic_scan(self):
        self.assertEqual(forbidden_tactics("by\n  rfl\n", ["simp", "aesop"]), [])
        self.assertEqual(forbidden_tactics("by\n  simp\n", ["simp", "aesop"]), ["simp"])

    def test_axiom_parser(self):
        name = "MatematicaAbierta.MCL.U00.L01.dos_es_dos"
        self.assertEqual(
            parse_axioms(f"'{name}' does not depend on any axioms", name),
            ("parsed", [])
        )
        self.assertEqual(
            parse_axioms(f"'{name}' depends on axioms: [propext, Quot.sound]", name),
            ("parsed", ["propext", "Quot.sound"])
        )
        self.assertEqual(parse_axioms("error: bad", name)[0], "rejected")


class TestMCLRunnerPolicy(unittest.TestCase):
    def setUp(self):
        self.spec = {
            "module": "MatematicaAbierta.MCL.U00.L01_Proposiciones",
            "max_submission_chars": 2000,
            "security": {
                "forbidden_constructs": [
                    "import", "namespace", "section", "end", "set_option",
                    "#", "unsafe", "axiom", "theorem", "def", "macro",
                    "syntax", "elab", "run_tac"
                ]
            },
            "exercises": [{
                "id": "MCL-U00-L01-E04",
                "theorem_prefix": "example : (10 : ℕ) = 10 := by",
                "allowed_tactics": ["rfl"],
                "forbidden_tactics": ["simp", "aesop", "omega", "norm_num"]
            }]
        }
        self.exercise = find_exercise(self.spec, "MCL-U00-L01-E04")
        self.security = dict(self.spec["security"])
        self.security["max_submission_chars"] = self.spec["max_submission_chars"]

    def test_rfl_is_pedagogically_accepted(self):
        result = policy_check("rfl\n", self.exercise, self.security)
        self.assertTrue(result["accepts"])
        self.assertEqual(result["tactic_heads"], ["rfl"])

    def test_simp_can_be_kernel_correct_but_policy_rejected(self):
        result = policy_check("simp\n", self.exercise, self.security)
        self.assertFalse(result["accepts"])
        self.assertIn("forbidden_tactic:simp", result["reasons"])
        self.assertIn("tactic_not_introduced:simp", result["reasons"])

    def test_structural_escape_is_rejected_by_policy(self):
        result = policy_check("set_option pp.all true in\nrfl\n", self.exercise, self.security)
        self.assertFalse(result["accepts"])
        self.assertIn("forbidden_construct:set_option", result["reasons"])

    def test_submission_rendering_stays_inside_proof(self):
        source = render_submission(self.spec["module"], self.exercise, "rfl")
        self.assertIn("import MatematicaAbierta.MCL.U00.L01_Proposiciones", source)
        self.assertIn("example : (10 : ℕ) = 10 := by\n  rfl", source)

    def test_tactic_heads(self):
        self.assertEqual(tactic_heads("-- comentario\nrfl\n"), ["rfl"])


if __name__ == "__main__":
    unittest.main()
