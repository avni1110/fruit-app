const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());

const PORT = 3000;

app.get("/api/health", (req, res) => {
    res.json({
        status: "ok"
    });
});

app.get("/api/fruits", (req, res) => {

    res.json([
        "Apple",
        "Strawberry",
        "Watermelon",
        "Orange",
        "Grapes"
    ]);

});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});