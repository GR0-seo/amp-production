exports.handler = async function(event, context) {
    const axios = require('axios');
    const parser = require('lambda-multipart-parser');

    const clientData = {
        "rellery": { apiKey: "PsYYrt", listId: "JTZTmW" },
    };
    
    const data = await parser.parse(event);

    console.log(data);

    const { apiKey, listId } = clientData[data.client];

    const res = await axios.post(`https://a.klaviyo.com/api/v2/list/${listId}/subscribe`, {
        api_key: apiKey,
        profiles: [{
            email: data.email
        }]
    }, { headers: { 'Content-Type': 'application/json' }});

    console.log(res);
    return { statusCode: res.status, body: JSON.stringify({ message: res.statusText })};
}
