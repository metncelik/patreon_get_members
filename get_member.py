import patreon

access_token = "YOUR CREATOR ACCESS TOKEN"
api_client = patreon.API(access_token)
campaign_id = api_client.get_campaigns(1).data()[0].id()

def get_members():
    members_response = api_client.get_campaigns_by_id_members(campaign_id, page_size=200, 
        includes={"currently_entitled_tiers": ["title", "amount_cents"]}, 
        fields={"member": ["full_name", "email", "patron_status"]}
        ).data()

    active_members = {}

    for member in members_response:
        is_active = member.attribute('patron_status') == "active_patron"

        if is_active:
            email = member.attribute('email')
            entitled_tiers = [tier.id() for tier in member.relationship('currently_entitled_tiers')]

            active_members[email]={
                "email":email,
                "entitled_tiers": entitled_tiers
            }
            
    return active_members
if __name__ == "__main__":
    get_members()
