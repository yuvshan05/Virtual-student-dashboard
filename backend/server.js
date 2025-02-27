import app from "./app.js";
const PORT = process.env.PORT;
import {v2 as cloudinary} from 'cloudinary';
import Razorpay from "razorpay"; 
         
// cloudinary configuration
cloudinary.config({ 
  cloud_name: 'dzspkf3x9', 
  api_key: '276711715475617', 
  api_secret: 'AK9pyygHdO-f5EUXmALymPcv0IE' // Click 'View API Keys' above to copy your API secret
});

// razorpay  
export const razorpay = new Razorpay({
  key_id: process.env.RAZORPAY_KEY_ID,
  key_secret: process.env.RAZORPAY_SECRET
})

app.listen(PORT, () => {
    console.log(`server started at http://localhost:${PORT}`);
})