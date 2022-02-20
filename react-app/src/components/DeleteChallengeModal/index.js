import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import { NavLink } from 'react-router-dom';
import DeleteChallengeForm from './DeleteChallengeForm';

function DeleteChallengeModal({ challenge }) {
    const [showModal, setShowModal] = useState(false);
    console.log("inside delete modal")
    console.log("challenge", challenge)
    return (
        <>{console.log("inside delete modal return")}
            <button
                onClick={(e) => {
                    setShowModal(true);
                    console.log("showModal", showModal)
                }}
                to=""
                className=''>DELETE
                {/* <i className="fa-solid fa-trash"></i> */}
            </button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <DeleteChallengeForm />
                    {/* <DeleteChallengeForm setShowModal={setShowModal} challenge={challenge} /> */}
                </Modal>
            )}
        </>
    );
}

export default DeleteChallengeModal;
