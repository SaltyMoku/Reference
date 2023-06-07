#include <windows.h>

int main(void)
{
	MessageBoxW(
		NULL,
		L"MessageBox text",
		L"MessageBox title",
		MB_YESNOCANCEL | MB_ICONEXCLAMATION
	);
	return EXIT_SUCCESS;
}
