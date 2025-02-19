from sar_project.agents.base_agent import SARBaseAgent
import google.generativeai as genai


gemini_api_key = 'AIzaSyC6AWqSlK1JWRIe79kwR48-WOr9WKplzy8'
class FirstAidAgent(SARBaseAgent):
    def __init__(self, name="first_aid_specialist"):
        super().__init__(
            name=name,
            role="First Aid Specialist",
            system_message="""You are a first aid specialist for Search and Rescue operations. Your role is to:
            1. Provide first aid instructions
            2. Advise on best medical practices
            Your information is for people who are 
            Only respond with a header for each of the above tasks, with the information about each underneath. Do not provide any commentary or additional information.
            For the first task, use the header, "First Aid Instrucions", for the second task use the header "Best Medical Practices".
            If you provide a numbered list for either set of instructions, do NOT use any new line characters."""
        )
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash",system_instruction=self.system_message)

    def process_request(self, message):
        """Process first aid related requests"""
        try:
            response_dict = {'Message': message,
                             'First Aid Instructions':None,
                             'Best Medical Practices':None,
                             'Full response text':None}
            response = self.model.generate_content(message)
            txt = response.text
            response_dict['Full response text'] = txt

            txt = txt.replace('1. First Aid Instructions','First Aid Instructions')
            txt = txt.replace('2. Best Medical Practices','Best Medical Practices')
            txt = txt.replace('**','')

            resp_l = txt.split('Best Medical Practices')
            response_dict['Best Medical Practices'] = resp_l[-1].strip()
            resp1 = [i.strip() for i in resp_l[0].split('\n\n') if len(i.strip()) > 3]
            response_dict['First Aid Instructions'] = resp1[-1]

            return response_dict
        except Exception as e:
            return {"error": str(e)}

    def update_status(self, status):
        """Update the agent's status"""
        self.status = status
        return {"status": "updated", "new_status": status}

    def get_status(self):
        """Get the agent's current status"""
        return getattr(self, "status", "unknown")