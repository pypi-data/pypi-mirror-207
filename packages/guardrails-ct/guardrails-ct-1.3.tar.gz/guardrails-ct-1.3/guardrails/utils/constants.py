import os

from lxml import etree as ET


class ConstantsContainer:
    def __init__(self):
        self._constants = {}
        self.fill_constants()

    def fill_constants(self) -> None:
        
        xml = """
        <constants>


<json_suffix_prompt>
Return a valid JSON object that respects this XML format and extracts only the information requested in this document. Respect the types indicated in the XML -- the information you extract should be converted into the correct 'type'. Try to be as correct and concise as possible. Find all relevant information in the document. If you are unsure of the answer, enter 'None'. If you answer incorrectly, you will be asked again until you get it right which is expensive.
</json_suffix_prompt>


<xml_prefix_prompt>
Given below is XML that describes the information to extract from this document and the tags to extract it into.
</xml_prefix_prompt>


<json_suffix_prompt_v2>
ONLY return a valid JSON object (no other text is necessary). The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise. If you are unsure anywhere, enter "None".
</json_suffix_prompt_v2>


<json_suffix_prompt_v2_wo_none>
ONLY return a valid JSON object (no other text is necessary). The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise.
</json_suffix_prompt_v2_wo_none>



<high_level_reask_prompt>
I was given the following JSON response, which had problems due to incorrect values.

{previous_response}

Help me correct the incorrect values based on the given error messages.
</high_level_reask_prompt>


<complete_json_suffix>
Given below is XML that describes the information to extract from this document and the tags to extract it into.

{output_schema}

ONLY return a valid JSON object (no other text is necessary), where the key of the field in JSON is the `name` attribute of the corresponding XML, and the value is of the type specified by the corresponding XML's tag. The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise. If you are unsure anywhere, enter `None`.

Here are examples of simple (XML, JSON) pairs that show the expected behavior:
- `<![CDATA[<string name='foo' format='two-words lower-case' />`]]> => `{{{{'foo': 'example one'}}}}`
- `<![CDATA[<list name='bar'><string format='upper-case' /></list>]]>` => `{{{{"bar": ['STRING ONE', 'STRING TWO', etc.]}}}}`
- `<![CDATA[<object name='baz'><string name="foo" format="capitalize two-words" /><integer name="index" format="1-indexed" /></object>]]>` => `{{{{'baz': {{{{'foo': 'Some String', 'index': 1}}}}}}}}`
</complete_json_suffix>

<complete_json_suffix_v2>
Given below is XML that describes the information to extract from this document and the tags to extract it into.

{output_schema}

ONLY return a valid JSON object (no other text is necessary), where the key of the field in JSON is the `name` attribute of the corresponding XML, and the value is of the type specified by the corresponding XML's tag. The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise.

Here are examples of simple (XML, JSON) pairs that show the expected behavior:
- `<![CDATA[<string name='foo' format='two-words lower-case' />`]]> => `{{{{'foo': 'example one'}}}}`
- `<![CDATA[<list name='bar'><string format='upper-case' /></list>]]>` => `{{{{"bar": ['STRING ONE', 'STRING TWO', etc.]}}}}`
- `<![CDATA[<object name='baz'><string name="foo" format="capitalize two-words" /><integer name="index" format="1-indexed" /></object>]]>` => `{{{{'baz': {{{{'foo': 'Some String', 'index': 1}}}}}}}}`
</complete_json_suffix_v2>


<json_suffix_prompt_examples>
ONLY return a valid JSON object (no other text is necessary), where the key of the field in JSON is the `name` attribute of the corresponding XML, and the value is of the type specified by the corresponding XML's tag. The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise. If you are unsure anywhere, enter `None`.

Here are examples of simple (XML, JSON) pairs that show the expected behavior:
- `<![CDATA[<string name='foo' format='two-words lower-case' />`]]> => `{{{{'foo': 'example one'}}}}`
- `<![CDATA[<list name='bar'><string format='upper-case' /></list>]]>` => `{{{{"bar": ['STRING ONE', 'STRING TWO', etc.]}}}}`
- `<![CDATA[<object name='baz'><string name="foo" format="capitalize two-words" /><integer name="index" format="1-indexed" /></object>]]>` => `{{{{'baz': {{{{'foo': 'Some String', 'index': 1}}}}}}}}`
</json_suffix_prompt_examples>


</constants>
        """

        parser = ET.XMLParser(encoding="utf-8")
        parsed_constants = ET.fromstring(xml, parser=parser)

        for child in parsed_constants:
            if isinstance(child, ET._Comment):
                continue
            if isinstance(child, str):
                continue

            constant_name = child.tag
            constant_value = child.text
            self._constants[constant_name] = constant_value

    def __getitem__(self, key):
        return self._constants[key]

    def __setitem__(self, key, value):
        self._constants[key] = value

    def __delitem__(self, key):
        del self._constants[key]

    def __iter__(self):
        return iter(self._constants)

    def __len__(self):
        return len(self._constants)

    def __contains__(self, key):
        return key in self._constants

    def __repr__(self):
        return repr(self._constants)

    def __str__(self):
        return str(self._constants)

    def items(self):
        return self._constants.items()

    def keys(self):
        return self._constants.keys()

    def values(self):
        return self._constants.values()


constants = ConstantsContainer()
