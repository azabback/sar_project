import pytest
from sar_project.agents.first_aid_agent import FirstAidAgent

class TestFirstAidAgent:
    @pytest.fixture
    def agent(self):
        return FirstAidAgent()

    def test_initialization(self, agent):
        assert agent.name == "first_aid_specialist"
        assert agent.role == "First Aid Specialist"
        assert agent.mission_status == "standby"

    def test_process_request(self, agent):
        message = "I hit my nose on a tree and my nose is bleeding"
        response = agent.process_request(message)
        assert "Message" in list(response.keys())
        assert "First Aid Instructions" in list(response.keys())
        assert "Best Medical Practices" in list(response.keys())
        assert "Full response text" in list(response.keys())
        assert len(response["First Aid Instructions"]) > 10
        assert len(response["Best Medical Practices"]) > 10

    def test_status_update(self, agent):
        response = agent.update_status("active")
        assert response["new_status"] == "active"
        assert agent.get_status() == "active"
