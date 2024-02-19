## Overview

The [StructureConfig](../../reference/griptape/config/structure_config.md) class allows for the customization of Structures within Griptape, enabling specific settings such as Drivers to be defined for Tasks. 

### Premade Configs

Griptape provides predefined [StructureConfig](../../reference/griptape/config/structure_config.md)'s for widely used services that provide APIs for most Driver types Griptape offers.

#### OpenAI

The [OpenAI Structure Config](../../reference/griptape/config/structure_config.md#griptape.config.structure_config.OpenStructureAIConfig) provides default Drivers for OpenAI's API's. This is the default config for all Structures.


```python
from griptape.config import OpenAIStructureConfig

agent = Agent(
    config=OpenAIStructureConfig()
)

agent = Agent() # This is equivalent to the above
```

#### Amazon Bedrock
The [Amazon Bedrock Structure Config](../../reference/griptape/config/structure_config.md#griptape.config.structure_config.AmazonBedrockStructureConfig) provides default Drivers for Amazon Bedrock's API's.

```python
from griptape.config import AmazonBedrockStructureConfig

agent = Agent(
    config=AmazonBedrockStructureConfig()
)
```

### Custom Configs

You can create your own [StructureConfig](../../reference/griptape/config/structure_config.md) by overriding the Drivers in [default_config](../../reference/griptape/config/structure_config.md#griptape.config.structure_config.StructureConfig.default_config).
The [StructureConfig](../../reference/griptape/config/structure_config.md) class includes "Dummy" Drivers for all types, which throw a [DummyException](../../reference/griptape/exceptions/dummy_exception.md) if invoked without being overridden. 
This approach ensures that you are informed through clear error messages if you attempt to use Structures without proper Driver configurations.

```python
from griptape.structures import Agent
from griptape.config import StructureConfig, StructureGlobalDriversConfig
from griptape.drivers import AnthropicPromptDriver

agent = Agent(
    config=StructureConfig(
        global_drivers=StructureGlobalDriversConfig(
            prompt_driver=AnthropicPromptDriver(
                model="claude-2",
                api_key=os.environ["ANTHROPIC_API_KEY"],
            )
        )
    ),
)
```

### Task Memory

Griptape allows for detailed control over [Task Memory](./task-memory.md) settings, permitting overrides on a per Engine basis, beyond the global Drivers configuration.

```python
from griptape.structures import Agent
from griptape.config import StructureConfig, StructureTaskMemoryConfig, StructureTaskMemoryQueryEngineConfig
from griptape.drivers import LocalVectorStoreDriver, OpenAiEmbeddingDriver


agent = Agent(
    config=StructureConfig(
        task_memory=StructureTaskMemoryConfig(
            query_engine=StructureTaskMemoryQueryEngineConfig(
                vector_store_driver=LocalVectorStoreDriver(
                    embedding_driver=OpenAiEmbeddingDriver(),
                )
            )
        )
    )
)
```

### Loading/Saving Configs

Configuration classes in Griptape offer utility methods for loading, saving, and merging configurations, streamlining the management of complex setups.

```python
from griptape.structures import Agent
from griptape.config import AmazonBedrockStructureConfig
from griptape.drivers import AmazonBedrockCohereEmbeddingDriver

custom_config = AmazonBedrockStructureConfig()
custom_config.global_drivers.embedding_driver = AmazonBedrockCohereEmbeddingDriver()
custom_config.merge_config(
    {
        "task_memory": {
            "summary_engine": {
                "prompt_driver": {
                    "model": "amazon.titan-text-express-v1",
                    "prompt_model_driver": {
                        "type": "BedrockTitanPromptModelDriver",
                    },
                }
            }
        }
    }
)
serialized_config = custom_config.to_json()
deserialized_config = AmazonBedrockStructureConfig.from_json(serialized_config)

agent = Agent(
    config=deserialized_config,
)
```

