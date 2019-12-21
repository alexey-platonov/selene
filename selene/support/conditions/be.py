# MIT License
#
# Copyright (c) 2015-2019 Iakiv Kramarenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import warnings

from selene import match
from selene.common.helpers import warn
from selene.condition import Condition


visible = match.element_is_visible
hidden = match.element_is_hidden

present = match.element_is_present
in_dom = match.element_is_present    # todo: do we need both present and in_dom?
existing = match.element_is_present  # todo: consider deprecating

absent = match.element_is_absent

enabled = match.element_is_enabled
disabled = match.element_is_disabled

blank = match.element_is_blank


# --- Deprecated --- #


def not_(condition_to_be_inverted: Condition):
    warnings.warn('might be deprecated; use Condition.as_not instead', PendingDeprecationWarning)
    return condition_to_be_inverted.not_


clickable = warn('might be deprecated', PendingDeprecationWarning)\
    .when(lambda: match.element_is_visible.and_(match.element_is_enabled))


empty = warn('might be deprecated, use have.size(0) instead', PendingDeprecationWarning) \
    .when(lambda: match.collection_has_size(0))

or_not_to_be = warn('deprecated, probably you have never used it:)', DeprecationWarning) \
    .when(lambda: None)
