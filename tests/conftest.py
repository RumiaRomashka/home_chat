#Это специальный файл pytest.

#В нём мы будем хранить нашу фикстуру — 
# подготовленный объект, который pytest 
# сможет автоматически передавать тестам.

from unittest.mock import AsyncMock, Mock

import pytest


@pytest.fixture
def mock_session():
    session = AsyncMock()

    result = Mock()
    result.scalar.return_value = 1

    session.execute.return_value = result

    return session