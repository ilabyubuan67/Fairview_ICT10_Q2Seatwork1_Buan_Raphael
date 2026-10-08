from pyscript import document, display 

club_members = [
    "Raphael Buan",
    "Jan Cabading",
    "Maggie Chiong",
    "Parminder Bhullar",
    "Ian Salangsang",
    "Dustin Cunanan",
    "Jacque Tian",
    "Carlos David",
]

def verify_member(event):

    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    member_name = f"{first_name} {last_name}"

  
    is_member = member_name in club_members

    congratulations_message = (
        f"Congratulations {member_name}! "
        "You are now part of the ICT club."
    )

    sorry_message = (
        f"Sorry {member_name}, "
        "your name is not on the list."
    )

    result_message = {
        True: congratulations_message,
        False: sorry_message
    }[is_member]

    document.getElementById("result").innerText = result_message



