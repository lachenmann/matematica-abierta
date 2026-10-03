import unittest

from adapters.mcl import forbidden_tactics, parse_axioms, validate_mapping, validate_profile


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


if __name__ == "__main__":
    unittest.main()
