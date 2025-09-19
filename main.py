from pyscript import display, document

def show_message(e):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    # Multiline string
    message = f""" 𝚂𝚝𝚞𝚍𝚎𝚗𝚝 𝙿𝚛𝚘𝚏𝚒𝚕𝚎 💙
Name 𓆝 𓆟 𓆞 𓆝 𓆟  : {name}
Age   𓆝 𓆟 𓆞 𓆝 𓆟 : {age}
School 𓆝 𓆟 𓆞 𓆝 𓆟: {school}

 𝙽𝚘𝚝𝚎𝚜 💙:
{name} 𝚒𝚜 𝚌𝚞𝚛𝚛𝚎𝚗𝚝𝚕𝚢 {age} 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍 𝚊𝚗𝚍 𝚜𝚝𝚞𝚍𝚒𝚎𝚜 𝚊𝚝 {school}.
𝚃𝚑𝚒𝚜 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚠𝚊𝚜 𝚐𝚊𝚝𝚑𝚎𝚛𝚎𝚍 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚒𝚗𝚙𝚞𝚝 𝚏𝚒𝚎𝚕𝚍𝚜 𝚊𝚗𝚍 𝚍𝚒𝚜𝚙𝚕𝚊𝚢𝚎𝚍 𝚞𝚜𝚒𝚗𝚐 𝚊 𝚖𝚞𝚕𝚝𝚒𝚕𝚒𝚗𝚎 𝚜𝚝𝚛𝚒𝚗𝚐 𝚒𝚗 𝙿𝚢𝚝𝚑𝚘𝚗 𝚟𝚒𝚊 𝙿𝚢𝚂𝚌𝚛𝚒𝚙𝚝.
"""

    display(message, target="output")