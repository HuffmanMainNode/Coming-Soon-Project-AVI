import unittest
from scripts.validate_project_manifest import validate

class ManifestTests(unittest.TestCase):
    def valid(self):
        return {
            "schema_version": "1.0.0",
            "project": "Project AVI",
            "full_name": "Advanced Virtual Intelligence System",
            "repository": "https://github.com/HuffmanMainNode/Coming-Soon-Project-AVI",
            "status": "announcement",
            "maturity": "pre-implementation",
            "design_pillars": ["decentralization"],
            "implemented_capabilities": [],
            "planned_capabilities": ["local-first architecture"],
            "runtime_required": False,
            "license_status": "not_declared",
            "limitations": ["No application code is present."]
        }

    def test_valid_announcement_manifest(self):
        self.assertEqual(validate(self.valid()), [])

    def test_announcement_cannot_claim_implemented_features(self):
        data = self.valid()
        data["implemented_capabilities"] = ["autonomous agent runtime"]
        self.assertIn(
            "announcement status requires an empty implemented_capabilities list",
            validate(data),
        )

    def test_rejects_missing_and_unexpected_fields(self):
        data = self.valid()
        del data["status"]
        data["unreviewed_claim"] = True
        errors = validate(data)
        self.assertTrue(any("missing fields" in item for item in errors))
        self.assertTrue(any("unexpected fields" in item for item in errors))

    def test_rejects_unknown_lifecycle_state(self):
        data = self.valid()
        data["status"] = "fully_operational"
        self.assertTrue(any("lifecycle" in item for item in validate(data)))

if __name__ == "__main__":
    unittest.main()
