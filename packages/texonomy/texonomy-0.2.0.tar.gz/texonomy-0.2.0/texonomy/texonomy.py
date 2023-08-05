from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from . import templates

# Levels of indentation for LaTeX code
INDENTATION = [" " * 4 * i for i in range(5)]

# Some common cardinalities.
ONE_TO_ONE = ((0, 1), (0, 1))
ONE_TO_MANY = ((0, -1), (0, 1))
MANY_TO_ONE = ((0, 1), (0, -1))
MANY_TO_MANY = ((0, -1), (0, -1))
MANY_TO_EXACTLY_ONE = ((1, 1), (0, -1))
EXACTLY_ONE_TO_MANY = ((0, -1), (1, 1))


class Direction(Enum):
    """An enum wrapping the relative position of an entity in the ERD."""

    ABOVE = "above"
    BELOW = "below"
    RIGHT = "right"
    LEFT = "left"


@dataclass
class Entity:
    """An object representing an entity in the diagram.

    Attributes:
        name (`str`): The display name of the entity.
        attributes (:obj:`list` of str): A list of this entity's
            attributes, which are displayed on the diagram.
        primary (`int`): The index of the primary key in the attributes list
            (by default it's 0).
        weak (`bool`): True if the entity is weak, False if not.
    """

    name: str
    attributes: List[str]
    primary: int
    weak: bool

    def __init__(self, name: str, attributes: List[str], weak: bool = False) -> None:
        """Initializes an Entity object.

        Args:
            name (`str`): The display name of the entity.
            attributes (:obj:`list` of `str`): A list of this entity's
                attributes, which are displayed on the diagram.
            weak (`bool`): True if the entity is weak, False if not. Defaults
                to False.
        """
        self.name = name
        self.weak = weak
        self.attributes = []
        for attribute in attributes:
            self.attributes.append(attribute)
        # the first attribute specified will defualt to the primary key
        self.primary = 0 if self.attributes else -1

    def __str__(self) -> None:
        """Formats an `Entity`'s fields in a readable way."""
        return (
            f"{self.name} ({'Weak ' if self.weak else ''}Entity)\n"
            f"Attributes: {self.attributes}\n\n"
            f"Primary: {'None' if self.primary == -1 else self.attributes[self.primary]}"
        )

    def add_attribute(self, attribute: str) -> None:
        """Adds an attribute to the end of the `Entity`'s attributes list.

        Args:
            attribute (`str`): The attribute to be added to the list.
        """
        self.attributes.append(attribute)

    def set_primary(self, attribute: str) -> None:
        """Sets the primary key to an existing attribute, referenced by name.

        Args:
            attribute (`str`): The name of the attribute to be set as new
                primary key.

        Raises:
            `ValueError`: If `attribute` does not exist in the Entity's list of
                attributes.
        """
        for idx, att in enumerate(self.attributes):
            if att == attribute:
                self.primary = idx
                return
        raise ValueError("This attribute doesn't exist.")

    # TODO: deal with empty attributes
    def to_latex(self) -> str:
        """Generates the LaTeX code associated with this Entity object.

        Returns:
            `str`: The LaTeX code, as a string.
        """
        code = f"{{{'weak' if self.weak else ''}" f"entity={{{id(self)}}}{{{self.name}}}{{%"
        for idx, attribute in enumerate(self.attributes):
            code += f"\n{INDENTATION[-1]}"
            code += (
                fr"\{'dashuline' if self.weak else 'underline'}" fr"{{{attribute}}}\\"
                if idx == self.primary
                else fr"{attribute}\\"
            )
        return code + f"\n{INDENTATION[-2]}}}}};"


@dataclass
class Relationship:
    """An object representing a relationship between two entities in the diagram.

    Attributes:
        anchor (`Entity`): The existing entity in the diagram to which the new
            entity should be attached.
        new_entity (`Entity`): The new entity to attach to this diagram.
        label (str): The display label given to this relationship; will be
            shown on the diagram.
        cardinality (:obj:`Tuple` of two :obj:`Tuple`s of `int`): The
            cardinality of this relationship (e.g., one-to-many).
        direction (`Direction`): The relative positioning of the new entity
            with respect to the anchor entity.
        attributes (:obj:`list` of `str`, optional): The attributes attached to
            this relationship, if any.
    """

    anchor: Entity
    new_entity: Entity
    label: str
    cardinality: Tuple[Tuple[int, int], Tuple[int, int]]
    direction: Direction
    attributes: Optional[List[str]] = None

    def __str__(self):
        """Formats an `Entity`'s fields in a readable way."""
        return f"{self.label}: [{self.anchor.name} to {self.new_entity.name}]"

    def add_attribute(self, attribute: str) -> None:
        """Adds an attribute to the end of the `Relationship`'s attributes list.

        Args:
            attribute (`str`): The attribute to be added to the list.
        """
        self.attributes.append(attribute)

    def attributes_to_latex(self) -> str:
        """Generates the LaTeX code associated with this `Relationship`'s attributes.

        Returns:
            `str`: The LaTeX code, as a string.
        """
        code = f"{{relattribute={{a{id(self)}}}{{%"

        if len(self.attributes) == 1:
            return code + f"\n{INDENTATION[-1]}{self.attributes[0]}\n" f"{INDENTATION[-2]}}}}};"

        for attribute in self.attributes:
            code += f"\n{INDENTATION[-1]}{attribute}"
            code += r"\\"

        return code + f"\n{INDENTATION[-2]}}}}};"


def determine_line_type(cardinality: Tuple[Tuple[int, int], Tuple[int, int]], direction: int) -> str:
    if cardinality[0 + direction][0] == 0:
        if cardinality[1 - direction][1] == 1:
            return "one line arrow"
        elif cardinality[1 - direction][1] == -1:
            return "one line"
        else:
            # TODO: label line with cardinality in the form x..y
            raise ValueError("Unsupported cardinality")
    elif cardinality[0 + direction][0] == 1:
        # total participation
        if cardinality[1 - direction][1] == 1:
            return "double line arrow"
        elif cardinality[1 - direction][1] == -1:
            return "double line"
        else:
            # TODO: label line with cardinality in the form x..y
            raise ValueError("Unsupported cardinality")


def get_line_anchors(direction: Direction) -> Tuple[str, str]:
    if direction == Direction.ABOVE:
        return ("south", "north")
    if direction == Direction.BELOW:
        return ("north", "south")
    if direction == Direction.RIGHT:
        return ("west", "east")
    if direction == Direction.LEFT:
        return ("east", "west")


@dataclass
class ERDiagram:
    """An object representing the entity-relationship diagram.

    Attributes:
        entities (:obj:`list` of `Entity`): The entities in this diagram.
        code (`str`): The LaTeX code that corresponds to all the entities and
            relationships in this diagram.
    """

    entities: List[Entity]
    code: str

    def __init__(self, entity: Entity) -> None:
        """Initializes an ERDiagram object.

        Args:
            entity (`Entity`): The first entity in this diagram.
        """
        self.entities = [entity]
        self.code = fr"{INDENTATION[-2]}\pic {entity.to_latex()}" + "\n"

    def add_relationship(self, rel: Relationship, defining: bool = False) -> None:
        """Adds a relationship (and, therefore, another entity) to the ER diagram.

        Args:
            rel (`Relationship`): The Relationship object corresponding to one
                anchor entity (already in this diagram) and one new entity to
                be added to this diagram.
            defining (`bool`): True if this relationship is the defining
                relationship of a weak entity, False otherwise. Defaults to
                False.

        Raises:
            `ValueError`: If the anchor does not already exist in the diagram.
        """
        if rel.anchor not in self.entities:
            raise ValueError("Anchor does not exist in the diagram.")
        self.entities.append(rel.new_entity)

        # TODO: add space changing option

        # render relationship diamond
        self.code += (
            fr"{INDENTATION[-2]}\pic[{rel.direction.value}=3em "
            f"of {id(rel.anchor)}] {{{'def' if defining else ''}"
            f"relationship={{{id(rel)}}}{{{rel.label}}}}};\n"
        )

        # render other entity
        self.code += fr"{INDENTATION[-2]}\pic[{rel.direction.value}=3em "
        self.code += f"of {id(rel)}] {rel.new_entity.to_latex()}\n"

        line_type_one = determine_line_type(rel.cardinality, 0)
        line_type_two = determine_line_type(rel.cardinality, 1)
        line_anchors = get_line_anchors(rel.direction)

        # render line between anchor entity and relationship
        self.code += (
            fr"{INDENTATION[-2]}\draw[{line_type_one}] "
            f"({id(rel)}.{line_anchors[0]}) -- "
            f"({id(rel.anchor)}.{line_anchors[1]});\n"
        )

        # render line between new entity and relationship
        self.code += (
            fr"{INDENTATION[-2]}\draw[{line_type_two}] "
            f"({id(rel)}.{line_anchors[1]}) -- "
            f"({id(rel.new_entity)}.{line_anchors[0]});\n"
        )

        if rel.attributes:
            direction = (
                Direction.RIGHT
                if rel.direction == Direction.ABOVE or rel.direction == Direction.BELOW
                else Direction.ABOVE
            )

            line_anchors = get_line_anchors(direction)

            # Stick relationship attributes to the right of any vertical
            # relationship, and above any horizontal one.
            self.code += fr"{INDENTATION[-2]}\pic[{direction.value}=2em of "
            self.code += f"{id(rel)}] {rel.attributes_to_latex()}\n"
            # latex node id is "a" + rel id
            self.code += (
                fr"{INDENTATION[-2]}\draw[dashed line] ({id(rel)}."
                f"{line_anchors[1]}) -- (a{id(rel)}."
                f"{line_anchors[0]});\n"
            )

    def add_specialization(self, superclass: Entity, subclass: Entity) -> None:
        """Adds a specialization relationship to the ER diagram.

        Args:
            superclass (`Entity`): The Entity object corresponding to an
                anchor entity (must already exist in this diagram), from which
                the subclass will specialize.
            subclass (`Entity`): The Entity object corresponding to a new
                entity which is a specialization of the superclass entity.

        Raises:
            `ValueError`: If the superclass does not exist in the diagram.
        """
        if superclass not in self.entities:
            raise ValueError("Anchor does not exist in the diagram.")
        self.entities.append(subclass)

        # add other entity
        self.code += fr"{INDENTATION[-2]}\pic[below=3em of {id(superclass)}]"
        self.code += f" {subclass.to_latex()}\n"
        self.code += fr"{INDENTATION[-2]}\draw[specialization] "
        self.code += f"({id(subclass)}.north) -- ({id(superclass)}.south);\n"

    def to_latex(self) -> str:
        """Generates the LaTeX code associated with this diagram.

        Returns:
            `str`: The LaTeX code, as a string.
        """
        prelude = pkg_resources.read_text(templates, 'template.tex')

        return (
            prelude + f"{INDENTATION[0]}\\begin{{document}}\n"
            f"{INDENTATION[1]}\\begin{{center}}\n"
            f"{INDENTATION[2]}\\begin{{tikzpicture}}\n"
            + self.code
            + f"{INDENTATION[2]}\\end{{tikzpicture}}\n"
            + f"{INDENTATION[1]}\\end{{center}}\n"
            f"{INDENTATION[0]}\\end{{document}}\n"
        )
