import json, os, pathlib, urllib.parse, urllib.request

KEY=os.environ["DEEPGRAM_API_KEY"]
VOICE=os.environ.get("DEEPGRAM_VOICE","flux-sharon-en")
OUT=pathlib.Path("audio"); OUT.mkdir(exist_ok=True)
# trigger 2026-09-23
clips={
"greeting":"Thanks for calling BrightSpark Electrical, Sarah speaking. How can I help today?",
"identity":"Yes, I'm Sarah, the business's AI receptionist. I take enquiries and organise job details for the team.",
"safety_address":"Got it. If there's smoke, sparking or exposed live parts, keep clear and call emergency services if anyone is in immediate danger. What's the service address?",
"phone":"Thanks. What's the best callback number?",
"phone_retry":"Could you give me the best callback number, including the area or mobile number?",
"name":"Perfect. What name should I put the job under?",
"name_retry":"I just need the customer's name for the job card. What name should I use?",
"photo":"Thanks. If you can, attach a JobLens photo. It helps the electrician arrive prepared.",
"photo_prompt":"Attach the JobLens photo using the button on the job card, then I'll organise the booking.",
"booking":"Photo received. I've added it to the job. I have a demo appointment tomorrow at 9:30 AM. Would you like me to book it?",
"complete":"Done. I've prepared the enquiry for the electrician with your details and JobLens information. They'll have everything in one place.",
"price1":"I can't responsibly invent a price before a licensed electrician assesses the fault. I'll make sure they receive the details first.",
"price2":"I don't want to guess and mislead you. The cost depends on what the electrician finds on site. I've captured the job details for them.",
"price3":"I still can't quote it safely from the enquiry alone. The electrician can confirm pricing after assessment.",
"organised":"Your enquiry is already organised for the team. If anything changes, the electrician can update it from the job card.",
"no_problem":"No problem.",
"captured":"Your job is captured and ready for the electrician."
}
for name,text in clips.items():
    url="https://api.deepgram.com/v2/speak?"+urllib.parse.urlencode({"model":VOICE})
    req=urllib.request.Request(url,data=json.dumps({"text":text}).encode(),headers={"Authorization":"Token "+KEY,"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=60) as r:
        (OUT/(name+".mp3")).write_bytes(r.read())
    print("generated",name)
