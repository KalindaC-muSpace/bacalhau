package job

import (
	"fmt"
	"strings"
	"testing"

	"github.com/filecoin-project/bacalhau/pkg/storage"
	"github.com/stretchr/testify/require"
)

func explodeStringArray(arr []string) []storage.StorageSpec {
	results := []storage.StorageSpec{}
	for _, str := range arr {
		results = append(results, storage.StorageSpec{
			Engine: storage.StorageSourceIPFS,
			Path:   str,
		})
	}
	return results
}

func joinStringArray(arr []storage.StorageSpec) []string {
	results := []string{}
	for _, str := range arr {
		results = append(results, str.Path)
	}
	return results
}

func TestApplyGlobPattern(t *testing.T) {

	simpleFileList := []string{
		"/a",
		"/a/file1.txt",
		"/a/file2.txt",
		"/b",
		"/b/file1.txt",
		"/b/file2.txt",
	}

	videoFiles := []string{
		"/inputs",
		"/inputs/Bird flying over the lake.mp4",
		"/inputs/Calm waves on a rocky sea gulf.mp4",
		"/inputs/Prominent Late Gothic styled architecture.mp4",
	}

	videoFilesNoSlash := []string{}
	for _, videoFile := range videoFiles {
		videoFilesNoSlash = append(videoFilesNoSlash, strings.TrimPrefix(videoFile, "/"))
	}

	videoResults := []string{
		"/inputs/Bird flying over the lake.mp4",
		"/inputs/Calm waves on a rocky sea gulf.mp4",
		"/inputs/Prominent Late Gothic styled architecture.mp4",
	}

	testCases := []struct {
		name     string
		files    []string
		pattern  string
		basePath string
		outputs  []string
	}{
		{
			"top level folders",
			simpleFileList,
			"/*",
			"",
			[]string{"/a", "/b"},
		},
		{
			"everything",
			simpleFileList,
			"/**/*",
			"",
			simpleFileList,
		},
		{
			"only files in folders",
			simpleFileList,
			"/**/*.*",
			"",
			[]string{
				"/a/file1.txt",
				"/a/file2.txt",
				"/b/file1.txt",
				"/b/file2.txt",
			},
		},
		{
			"base path",
			[]string{
				"/a",
				"/a/file1.txt",
				"/a/file2.txt",
				"/a/file3.txt",
				"/a/file4.txt",
				"/a/apples.txt",
			},
			"/file*.txt",
			"/a",
			[]string{
				"/a/file1.txt",
				"/a/file2.txt",
				"/a/file3.txt",
				"/a/file4.txt",
			},
		},
		{
			"test with spaces in file names",
			videoFiles,
			"/inputs/*.mp4",
			"",
			videoResults,
		},
		{
			"test without leading slash in pattern",
			videoFiles,
			"*.mp4",
			"/inputs",
			videoResults,
		},
		{
			"test without leading slash in filenames",
			videoFilesNoSlash,
			"/*.mp4",
			"/inputs",
			videoResults,
		},
	}

	for _, testCase := range testCases {
		results, err := ApplyGlobPattern(explodeStringArray(testCase.files), testCase.pattern, testCase.basePath)
		require.NoError(t, err)
		require.Equal(
			t,
			strings.Join(testCase.outputs, ","),
			strings.Join(joinStringArray(results), ","),
			fmt.Sprintf("%s: %s did not result in correct answer", testCase.name, testCase.pattern),
		)
	}

}