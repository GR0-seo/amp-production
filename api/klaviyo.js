exports.handler = async function(event, context) {
    const axios = require('axios');
    const parser = require('lambda-multipart-parser');

    const clientData = {
        "rellery": { apiKey: "pk_7ae913cf07d68ffe6c3ffdd71d78452a56", listId: "JTZTmW" },
    };
    
    const data = await parser.parse(event);

    console.log(data);

    const { apiKey, listId } = clientData[data.client];

     return (await axios.post(`https://a.klaviyo.com/api/v2/list/${listId}/subscribe`, {
        api_key: apiKey,
        profiles: [{
            email: data.email
        }]
    }, { headers: { 'Content-Type': 'application/json' }}));
}
