# Welcome to the Platform for Domain-Specific-Language (DSL) Modeling Standard

The DSL is a human-readable, machine-comprehensible modeling notation.
On the basis of this standard, machine's knowledge shall become controllable, such as from a chatbot.
For instance, the chatbot's knowledge can be 
(1) visualized by importing it to a modeling tool,
(2) modified with the aid of the modeling tool by human knowledge experts, and
(3) prepared for training by exporting it from the modeling tool.

The tool was originally developed by Marcus Grum.


# How to prepare a modeling tool, such as Modelangelo

1. Install python 3 environment

`sudo pip install python3`

# How to roll out modeling items?

1. Copy item files from `$DslRepositoryPath/meta-model/modelangelo/dsl` to Modelangelo template folder `$ModelangeloPath/templates/dsl/`.

1. Start Modelangelo tool and create a new file based on the corresponding meta-model by clicking on menu bar `file/new/new Project`. At the dialogue window showing up, the corresponding meta-model can be selected.

1. Create domain-specific language visualization by manually dragging items from the palette of Modelangelo tool for testing.

# How to roll out scripts?

1. Create relevant files to be deployed by compilation.

```
cd $DslRepositoryPath
python -m compileall ./src
```

1. Copy files from `$DslRepositoryPath/src/__pycache__/` to Modelangelo script folder `$ModelangeloPath/scripts/dsl/src`.

1. Modify relevant `$ModelangeloPath/scripts/script-executions.json` file to be started by python command.

```
{
  "scriptExecutions" : [
   { ... },
   {
      "name" : "DSL-Importer: Transfer DSL files to Modelangelo files",
      "path" : "dsl/src/",
      "command" : "python ./importer.cpython-36.pyc"
   },
    {
      "name" : "DSL-Exporter: Transfer Modelangelo files to DSL files",
      "path" : "dsl/src/",
      "command" : "python ./exporter.cpython-36.pyc"
    }
  ]
}
```

1. Start Modelangelo tool and select corresponding script via menu bar. E.g select `scripts/DSL-Importer...` or `scripts/DSL-Exporter...` for testing.

# How to use dsl modeling notation for managing chatbot knowledge?

![Image of DSL Data Flow](./documentation/images/DSLDataFlow.png)

1. Copy relevant .xml files of dsl standard to `$ModelangeloPath/scripts/dsl/examples/import`. These represent the chatbot's, machine-readable knowledge.

1. Start Modelangelo tool and activate import script via menu bar `scripts/DSL-Importer: Transfer DSL files to Modelangelo files`. So, a human-readable visualization is constructed.

1. Load transformed .xml Modelangelo file via Modelangelo's menu bar `file/open` from `$ModelangeloPath/scripts/dsl/examples/modeling/DslExample.xml`. So, the human-readable chatbot knowledge is visualized by modeling tool.

1. Modify domain-specific language visualization manually by Modelangelo tool. For example, drag and drop items from modeling palette, delete them, search for knowledge, etc. Carry out a proper knowledge management.

1. Activate export script via menu bar `scripts/DSL-Exporter: Transfer Modelangelo files to DSL files`. So, the manipulated, human-readable knowledge base is exported to the chatbot's, machine-readable knowledge.

1. Copy relevant .xml files of dsl standard from `$ModelangeloPath/scripts/dsl/examples/export` to your chatbots knowledge base, so that the chatbot can consider the modified knowledge base.

# Publications

Grum M., Kotarski D., Ambros M., Biru T., Krallmann H., Gronau N. (2021) Managing Knowledge of Intelligent Systems - The Design of a Chatbot Using Domain-Specific Knowledge. In: Shishkov B. (eds) Business Modeling and Software Design. BMSD 2021. Lecture Notes in Business Information Processing, vol 422. Springer, Cham. https://doi.org/10.1007/978-3-030-79976-2_5

## Contributions

If you want to contribute, please review the contribution guidelines.

## License

GNU Affero General Public License v3.0