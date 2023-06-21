# sheetmusicclassifier

Fork of [this](https://github.com/apacha/MusicScoreClassifier) repo by [Alexander Pacha](https://github.com/apacha).

## Changes:

- Wrapped into a package
- Less chatty
- Batch analysis
- Return json data with results

## Usage:

You'll need to `pip install` the package.

### Classification:

```python
import sheetmusicclassifier as smc
from utils import writeJson

inputFiles = [
    "a-score.jpeg",
    "not-a-score.jpeg"
]

# Download the prebuilt model here: https://github.com/apacha/MusicScoreClassifier/releases (mobilenetv2.h5)
model = "model/mobilenetv2.h5"

processed = smc.process(model, inputFiles)

writeJson(processed, "data-output.json")
```

### Output:
```json
{
    "images": [
        {
            "path": "a-score.jpeg",
            "scores": [
                0.0,
                1.0
            ],
            "highest_prob": 1,
            "class": "score",
            "certainty": 1.0
        },
        {
            "path": "not-a-score.jpeg",
            "scores": [
                0.9999,
                0.0001
            ],
            "highest_prob": 0,
            "class": "other",
            "certainty": 0.9999
        }
    ]
}
```