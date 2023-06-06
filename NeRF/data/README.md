## Data
To get the official dataset, you need to download from [NeRF dataset](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1)
And unzip it to here with convention of
```
.
├── nerf_llff_data
│   ├── fern
│   ├── flower
│   ├── fortress
│   ├── horns
│   ├── leaves
│   ├── orchids
│   ├── pinecone
│   ├── room
│   ├── trex
│   └── vasedeck
└── nerf_synthetic
    ├── chair
    ├── drums
    ├── example
    ├── ficus
    ├── hotdog
    ├── lego
    ├── materials
    ├── mic
    ├── README.txt
    └── ship
```

To one of its case, it is just like this
```
.
├── test
├── train
├── transforms_test.json
├── transforms_train.json
├── transforms_val.json
└── val

```

And then customize the `./config/XXX.txt` file for your data.