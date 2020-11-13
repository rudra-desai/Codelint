/* eslint-disable react/prop-types */
import React from 'react';
import 'react-dropdown/style.css';
import './top.css';
import Dropmenu from './Dropmenu';

export default function Top({
  handleLinter, handleSelectedRepo, linter, repos, handleRepoTree, repoTreeFiles,
  selectedRepo, selectedFile,
}) {
  return (
    <>
      <div className="top">
        <h2>Codelint</h2>
        <Dropmenu
          handleDropdown={handleLinter}
          value={linter}
          className="dropdown"
          placeholder="Select a linter"
          options={['pylint', 'eslint']}
        />
        {repos.length !== 0
          ? (
            <Dropmenu
              handleDropdown={handleSelectedRepo}
              value={selectedRepo}
              className="dropdown"
              placeholder="Select a repo after GitHub Auth"
              options={repos}
            />
          ) : ''}
        {repoTreeFiles.length !== 0
          ? (
            <div className="files">
              <Dropmenu
                handleDropdown={handleRepoTree}
                value={selectedFile}
                className="allfiles"
                placeholder="Select a file after selecting Repo"
                options={repoTreeFiles}
              />
            </div>
          ) : ''}
      </div>
    </>
  );
}
