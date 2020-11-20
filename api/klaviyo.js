exports.handler = async function(event, context) {
    const axios = require('axios');
    const parser = require('lambda-multipart-parser');

    const clientData = {
        "rellery": { apiKey: "pk_7ae913cf07d68ffe6c3ffdd71d78452a56", listId: "JTZTmW", sms_consent: false },
        "ties": { apiKey: "pk_a370d9eb8f1aca15076a85e2063d8e11ee", listId: "JgrX6e", sms_consent: false },
    };
    
    const { client, files, ...data } = await parser.parse(event);
    console.log(data);

    const { apiKey, listId, sms_consent } = clientData[client];

    let submission = data;
    if (data.phone_number) {
        submission.sms_consent = sms_consent
    }

    const res = (await axios.post(`https://a.klaviyo.com/api/v2/list/${listId}/subscribe`, {
        api_key: apiKey,
        profiles: [submission]
    }, { headers: { 'Content-Type': 'application/json' }}));

    console.log(res)
    return { statusCode: res.status, body: JSON.stringify({ message: res.statusText })};
}
